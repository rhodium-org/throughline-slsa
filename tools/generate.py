#!/usr/bin/env python3
"""Generate the SLSA throughline source from tools/slsa_data.py.

SLSA v1.2 has two normative *tracks* — Build and Source — that are genuinely distinct
purposes, so this source is multi-root: one `intent` per track. Each track's requirement
*groups* become `user_requirement`s that `derives_from` the track's intent, and each
individual requirement becomes a `system_requirement` that `implements` its group, carrying
its track and minimum level.

Two invariants make re-running safe and faithful:

* **UIDs are permanent.** The mapping from a requirement's `source_ref` (its published SLSA
  name, e.g. ``Distribute provenance``) to a throughline UID is derived from the items
  already on disk. Existing items are never renumbered; only source_refs with no item yet
  get a freshly allocated UID, in document order, continuing from the highest number used.
* **Data-driven docs.** `docs/spec.md` is regenerated with blanked `tl:*` markers, so
  `tl docs` MUST run after this script (CI's `tl docs --check` enforces it).

Usage:  python tools/generate.py
"""
from __future__ import annotations

from pathlib import Path

import yaml

from slsa_data import EDITION, TRACKS

REPO = Path(__file__).resolve().parent.parent
INTENT_DIR = REPO / "intents"        # intent, prefix INT (fixed per-track UIDs)
GROUP_DIR = REPO / "groups"          # user_requirement, prefix UR
REQ_DIR = REPO / "requirements"      # system_requirement, prefix SR
SPEC = REPO / "docs" / "spec.md"


def _scan_existing(dir_: Path) -> dict[str, str]:
    """Map source_ref -> UID for the items already on disk."""
    ref2uid: dict[str, str] = {}
    for f in dir_.glob("*.yml"):
        data = yaml.safe_load(f.read_text(encoding="utf-8"))
        ref = (data.get("attrs") or {}).get("source_ref")
        if ref:
            ref2uid[ref] = data["uid"]
    return ref2uid


def _max_num(ref2uid: dict[str, str], prefix: str) -> int:
    nums = [int(u.split("-")[1]) for u in ref2uid.values() if u.startswith(prefix + "-")]
    return max(nums, default=0)


def _dump(path: Path, item: dict) -> None:
    path.write_text(
        yaml.safe_dump(item, sort_keys=False, allow_unicode=True, width=88),
        encoding="utf-8",
    )


SPEC_HEADER = """\
# SLSA {edition} — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful cut of **SLSA v{edition}**. SLSA defines two normative *tracks*
— Build and Source — and because they are genuinely distinct purposes, each is a root
`intent` of this graph. Every requirement *group* is a `user_requirement` that
`derives_from` its track's intent, and every requirement is a `system_requirement` that
`implements` its group, carrying its track in `attrs.slsa_track` and the minimum level at
which it becomes mandatory in `attrs.slsa_level`. The published SLSA requirement name lives
in `attrs.source_ref` (e.g. `Distribute provenance`); the throughline UIDs are this source's
own and immutable — a consumer cites a requirement as `slsa:SR-0003`, never by its name.

It carries
<!-- tl:count type == 'intent' -->
<!-- tl:end --> tracks,
<!-- tl:count type == 'user_requirement' -->
<!-- tl:end --> requirement groups and
<!-- tl:count type == 'system_requirement' -->
<!-- tl:end --> requirements.
"""


def generate_spec(intent_uid_by_track: dict[str, str],
                  group_ref2uid: dict[str, str]) -> None:
    """Write docs/spec.md: a hand-owned header plus, per track, its intent tl:item and,
    per group, the group tl:item and a tl:table of its requirements. `tl docs` injects the
    live content into the markers."""
    parts = [SPEC_HEADER.format(edition=EDITION)]
    for track in TRACKS:
        tname = track["track"]
        parts.append(f"## {tname} track\n")
        parts.append(f"<!-- tl:item {track['intent_uid']} -->\n<!-- tl:end -->\n")
        for group in track["groups"]:
            gref = group["source_ref"]
            parts.append(f"### {group['title']}\n")
            parts.append(f"<!-- tl:item {group_ref2uid[gref]} -->\n<!-- tl:end -->\n")
            flt = (
                "type == 'system_requirement' "
                f"and attrs.get('slsa_track') == '{tname}' "
                f"and attrs.get('slsa_group') == '{gref}'"
            )
            parts.append(f"<!-- tl:table {flt} -->\n<!-- tl:end -->\n")
    SPEC.write_text("\n".join(parts) + "\n", encoding="utf-8")


def main() -> int:
    group_ref2uid = _scan_existing(GROUP_DIR)
    req_ref2uid = _scan_existing(REQ_DIR)
    next_ur = _max_num(group_ref2uid, "UR") + 1
    next_sr = _max_num(req_ref2uid, "SR") + 1

    intent_uid_by_track: dict[str, str] = {}
    new_groups = new_reqs = 0

    for track in TRACKS:
        tname = track["track"]
        intent_uid = track["intent_uid"]
        intent_uid_by_track[tname] = intent_uid
        # Track root intent (fixed UID, non-normative, self-justifying — no links).
        _dump(INTENT_DIR / f"{intent_uid}.yml", {
            "uid": intent_uid,
            "type": "intent",
            "status": "approved",
            "title": track["title"],
            "text": track["text"],
            "normative": False,
            "attrs": {"source_ref": track["source_ref"]},
        })

        for group in track["groups"]:
            gref = group["source_ref"]
            if gref in group_ref2uid:
                guid = group_ref2uid[gref]
            else:
                guid = f"UR-{next_ur:04d}"
                next_ur += 1
                group_ref2uid[gref] = guid
                new_groups += 1
            _dump(GROUP_DIR / f"{guid}.yml", {
                "uid": guid,
                "type": "user_requirement",
                "status": "approved",
                "title": f"{tname} — {group['title']}",
                "text": group["text"],
                "links": [{"target": intent_uid, "type": "derives_from"}],
                "attrs": {"source_ref": gref, "slsa_track": tname},
            })

            for req in group["requirements"]:
                rref = req["source_ref"]
                if rref in req_ref2uid:
                    ruid = req_ref2uid[rref]
                else:
                    ruid = f"SR-{next_sr:04d}"
                    next_sr += 1
                    req_ref2uid[rref] = ruid
                    new_reqs += 1
                _dump(REQ_DIR / f"{ruid}.yml", {
                    "uid": ruid,
                    "type": "system_requirement",
                    "status": "approved",
                    "title": req["title"],
                    "text": req["text"],
                    "rationale": req["rationale"],
                    "links": [{"target": guid, "type": "implements"}],
                    "attrs": {
                        "source_ref": rref,
                        "slsa_track": tname,
                        "slsa_group": gref,
                        "slsa_level": req["level"],
                    },
                })

    generate_spec(intent_uid_by_track, group_ref2uid)

    print(f"intents: {len(intent_uid_by_track)} tracks")
    print(f"groups: {new_groups} new, {len(group_ref2uid)} total")
    print(f"requirements: {new_reqs} new, {len(req_ref2uid)} total")
    print(f"spec: {SPEC} regenerated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
