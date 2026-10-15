"""What `make_manifest.py` reads besides comparator JSON. Not a command-line tool.

The comparators and their CAM readers moved to recast-cesm (`scripts/compare/`,
CORRECTNESS-ORGANIZATION.md step 5); this is the part of their shared `dataio.py`
that assembling a record still needs: loading a benchmark document, listing the
candidate outputs to fingerprint, and the key that ties a benchmark rule to the
measurement a comparator made of it.

Every unreadable input raises `DataError`, which `make_manifest.py` turns into
exit 2 with nothing written.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, Optional, Sequence

INCLUDE_PREFIXES = ("h0.", "r.", "rh0.", "rs.")
SUPPORTED_SUFFIXES = (".nc", ".npy", ".npz", ".txt", ".csv", ".tab", ".dat")


class DataError(Exception):
    """An input could not be read. Always becomes exit 2, never a PASS."""


def rule_key(rule: dict) -> str:
    """Identity of an acceptance rule, ignoring `gating` and `note`.

    `make_manifest.py` matches a benchmark rule to the measurement a comparator
    produced by this key rather than by list position, so a benchmark edited
    between the comparison and the manifest is caught as an unevaluable rule
    instead of quietly binding a verdict to the wrong criterion. recast-cesm's
    `scripts/compare/compare_stats.py` writes the same key; the two must agree.
    """
    body = {k: v for k, v in rule.items() if k not in ("gating", "note")}
    return json.dumps(body, sort_keys=True)


# --------------------------------------------------------------------------
# run directory scanning


def cam_key(path: Path) -> Optional[str]:
    """Output identity with the case name stripped: the part after '.cam.'.

    Returns None for a name that carries no '.cam.' marker, which is how a
    non-output file in a run directory is skipped.
    """
    marker = ".cam."
    idx = path.name.find(marker)
    if idx < 0:
        return None
    return path.name[idx + len(marker):]


def collect_run_files(
    run_dir: Path, prefixes: Sequence[str] = INCLUDE_PREFIXES
) -> Dict[str, Path]:
    """Map key -> path for the outputs in scope, exactly as the PyCAM5 script did.

    In scope: `*.cam.*` whose stripped key starts with one of `prefixes` and
    whose suffix this module can read. The suffix set is wider than `.nc` so the
    tools are exercisable without NetCDF; the key rule is unchanged.
    """
    if not run_dir.is_dir():
        raise DataError("not a directory: %s" % run_dir)
    out: Dict[str, Path] = {}
    for path in sorted(run_dir.glob("*.cam.*")):
        if path.suffix not in SUPPORTED_SUFFIXES or not path.is_file():
            continue
        key = cam_key(path)
        if key is None or not key.startswith(tuple(prefixes)):
            continue
        if key in out:
            raise DataError(
                "two files in %s share the key %r: %s and %s"
                % (run_dir, key, out[key].name, path.name)
            )
        out[key] = path
    return out


# --------------------------------------------------------------------------
# documents


def load_document(path: Path) -> dict:
    """Read a JSON or YAML document — a benchmark file or an acceptance block.

    Benchmarks are YAML by convention, and PyYAML is not in the standard
    library. Rather than shipping a partial YAML reader whose disagreements
    with the real thing would surface as wrong acceptance criteria, a YAML
    document with no PyYAML installed is a DataError naming both ways out.
    """
    if not path.is_file():
        raise DataError("no such document: %s" % path)
    text = path.read_text()
    if path.suffix == ".json":
        try:
            return json.loads(text)
        except ValueError as exc:
            raise DataError("%s is not valid JSON: %s" % (path, exc)) from exc
    try:
        import yaml
    except ImportError:
        raise DataError(
            "cannot read %s: PyYAML is not installed. Install PyYAML, or supply "
            "the same document as .json." % path.name
        ) from None
    try:
        document = yaml.safe_load(text)
    except yaml.YAMLError as exc:
        raise DataError("%s is not valid YAML: %s" % (path, exc)) from exc
    if not isinstance(document, dict):
        raise DataError("%s does not hold a mapping" % path)
    return document
