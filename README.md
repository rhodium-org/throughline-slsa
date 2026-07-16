# throughline-slsa

**SLSA (Supply-chain Levels for Software Artifacts)** expressed as a
[throughline](https://pypi.org/project/throughline/) **source** — a standalone,
grounded requirements graph that a consuming project composes with
[throughline-compose](https://github.com/rhodium-org/throughline-compose).

This repository holds no application code. It is a directory of small YAML items with
permanent UIDs, validated by `tl check`. Consumers import it under a namespace and
reference its requirements as `slsa:SR-0003`.

## Status

This is the **SLSA v1.2** edition —
<!-- tl:count type == 'intent' -->
2
<!-- tl:end --> tracks,
<!-- tl:count type == 'user_requirement' -->
5
<!-- tl:end --> requirement groups and
<!-- tl:count type == 'system_requirement' -->
22
<!-- tl:end --> requirements, published to [`docs/spec.md`](docs/spec.md).

The counts above are rendered from the live graph by the `tl:count` directive, so they
cannot drift. Re-run [`tools/generate.py`](tools/generate.py) after editing
[`tools/slsa_data.py`](tools/slsa_data.py) to revise the graph; it preserves every existing
UID↔requirement mapping and only allocates UIDs for requirements that have none yet.

## Shape — two tracks, two roots

SLSA v1.2 defines **two normative tracks**, and they are two genuinely different purposes,
so this source has **two root intents** rather than one umbrella:

| Track | Root | Levels | What it grades |
|---|---|---|---|
| **Build** | `INT-0001` | L0–L3 | the integrity and provenance of the *build* that produced an artifact |
| **Source** | `INT-0002` | L1–L4 | the authorship, history and provenance of the *source revision* |

Under each track root:

- **Requirement groups** (Build: *Producer*, *Provenance generation*, *Isolation strength*;
  Source: *Organization*, *Source Control System*) are `user_requirement`s that
  `derives_from` their track's intent.
- **Individual requirements** are `system_requirement`s that `implements` their group,
  each carrying its track in `attrs.slsa_track` and the **minimum level at which it becomes
  mandatory** in `attrs.slsa_level` (the SLSA analogue of ASVS's L1/L2/L3). Levels are
  cumulative, so a requirement is recorded once, at the lowest level it applies.

## Modelling conventions

- **throughline UIDs are this source's own** (`SR-0001`…), immutable and never the SLSA
  requirement name. The published name lives in `attrs.source_ref`
  (`"Distribute provenance"`); the minimum level in `attrs.slsa_level`; the track in
  `attrs.slsa_track`.
- Root intents are **non-normative** — each track justifies itself; every group and
  requirement must trace to a root or `tl check` fails.

## Editions

SLSA versions itself (v0.1 → v1.0 was a full restructure; v1.1/v1.2 added the Source
track additively). Editions are **git tags** of this one repo (`v1.2` now); a future full
restructure would become a release branch, the way `throughline-asvs` handles v4 → v5.

## Composing it

In a consuming throughline project's `throughline.toml`:

```toml
[[sources]]
namespace = "slsa"
url = "https://github.com/timebacksolutions/throughline-slsa"
ref = "v1.2"
```

Then reference a requirement from your own items:

```yaml
links:
- target: slsa:SR-0006          # SLSA Build L3, "Provenance is unforgeable"
  type: satisfies
```

`tl-compose check` resolves the reference; bare `tl check` fails fast and points you at
`tl-compose`.

## Local checks

```sh
pip install throughline
tl check --strict     # the graph must stay sound
tl docs --check       # docs/spec.md must match the graph
```

## Provenance

SLSA is a project of the [Open Source Security Foundation (OpenSSF)](https://openssf.org/),
a Linux Foundation project, licensed CC BY 4.0. See [NOTICE](NOTICE) and
https://slsa.dev/spec/v1.2/. This repository is Apache-2.0 for its structure and tooling;
the reproduced requirement text remains the work of the OpenSSF and its contributors.
