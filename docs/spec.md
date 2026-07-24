# SLSA 1.2 — throughline source

This document is **generated from the graph** by `tl docs`; `tl docs --check` gates
it in CI. The prose headings are hand-owned — everything between `tl:*` markers is
injected from the YAML items, so the published spec can never drift from the graph.

This source is a faithful cut of **SLSA v1.2**. SLSA defines two normative *tracks*
— Build and Source — and because they are genuinely distinct purposes, each is a root
`intent` of this graph. Every requirement *group* is a `user_requirement` that
`derives_from` its track's intent, and every requirement is a `system_requirement` that
`implements` its group, carrying its track in `attrs.slsa_track` and the minimum level at
which it becomes mandatory in `attrs.slsa_level`. The published SLSA requirement name lives
in `attrs.source_ref` (e.g. `Distribute provenance`); the throughline UIDs are this source's
own and immutable — a consumer cites a requirement as `slsa:SR-0003`, never by its name.

It carries
<!-- tl:count type == 'intent' -->
2
<!-- tl:end --> tracks,
<!-- tl:count type == 'user_requirement' -->
5
<!-- tl:end --> requirement groups and
<!-- tl:count type == 'system_requirement' -->
22
<!-- tl:end --> requirements.

## Build track

<!-- tl:item INT-0001 -->
**INT-0001 — Software artifacts are built with verifiable integrity and provenance** — `intent`, status `approved`

> The SLSA Build track exists so that a software artifact is produced by a build process whose integrity and provenance can be verified against graded levels (Build L0 through L3). Higher levels move from provenance merely existing, through provenance signed by a hosted platform, to hardened builds whose provenance is strongly resistant to forgery — giving consumers a graded basis for trusting how an artifact was produced rather than ad-hoc judgement.

**source_ref**: Build track
<!-- tl:end -->

### Producer

<!-- tl:item UR-0001 -->
**UR-0001 — Build — Producer** — `user_requirement`, status `approved`

> Requirements on the producer — the organization that owns and releases the software — to choose a capable build platform, build consistently, and distribute provenance to consumers.

*Derives from:* INT-0001

**source_ref**: Producer · **slsa_track**: Build
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('slsa_track') == 'Build' and attrs.get('slsa_group') == 'Producer' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0001 | system_requirement | approved | Choose an appropriate build platform |
| SR-0002 | system_requirement | approved | Follow a consistent build process |
| SR-0003 | system_requirement | approved | Distribute provenance |
<!-- tl:end -->

### Provenance generation

<!-- tl:item UR-0002 -->
**UR-0002 — Build — Provenance generation** — `user_requirement`, status `approved`

> Requirements on the build platform to generate provenance that describes how a package was produced, and to make that provenance authentic and then unforgeable as the Build level rises.

*Derives from:* INT-0001

**source_ref**: Provenance generation · **slsa_track**: Build
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('slsa_track') == 'Build' and attrs.get('slsa_group') == 'Provenance generation' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0004 | system_requirement | approved | Provenance exists |
| SR-0005 | system_requirement | approved | Provenance is authentic |
| SR-0006 | system_requirement | approved | Provenance is unforgeable |
<!-- tl:end -->

### Isolation strength

<!-- tl:item UR-0003 -->
**UR-0003 — Build — Isolation strength** — `user_requirement`, status `approved`

> Requirements on the build platform to run builds on hosted infrastructure and, at higher levels, in an isolated environment free of unintended external influence.

*Derives from:* INT-0001

**source_ref**: Isolation strength · **slsa_track**: Build
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('slsa_track') == 'Build' and attrs.get('slsa_group') == 'Isolation strength' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0007 | system_requirement | approved | Hosted |
| SR-0008 | system_requirement | approved | Isolated |
<!-- tl:end -->

## Source track

<!-- tl:item INT-0002 -->
**INT-0002 — Source revisions have verifiable authorship, history and provenance** — `intent`, status `approved`

> The SLSA Source track exists so that the authoring, review and management of source code can be verified against graded levels (Source L1 through L4). Higher levels move from source merely being version-controlled, through continuous, attested history and provenance, to continuously enforced technical controls and two-party review — giving consumers a graded basis for trusting how a source revision was produced, everything that happens before a revision reaches a builder.

**source_ref**: Source track
<!-- tl:end -->

### Organization

<!-- tl:item UR-0004 -->
**UR-0004 — Source — Organization** — `user_requirement`, status `approved`

> Requirements on the organization that produces source revisions — to choose a capable source control system, control access and enforce history, and (at higher levels) continuously enforce technical controls.

*Derives from:* INT-0002

**source_ref**: Organization · **slsa_track**: Source
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('slsa_track') == 'Source' and attrs.get('slsa_group') == 'Organization' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0009 | system_requirement | approved | Choose an appropriate source control system |
| SR-0010 | system_requirement | approved | Configure the SCS to control access and enforce history |
| SR-0011 | system_requirement | approved | Safe expunging process |
| SR-0012 | system_requirement | approved | Continuous technical controls |
<!-- tl:end -->

### Source Control System

<!-- tl:item UR-0005 -->
**UR-0005 — Source — Source Control System** — `user_requirement`, status `approved`

> Requirements on the source control system (SCS) — to make repositories and revisions identifiable and immutable, expose human-readable changes, and issue verifiable attestations about how revisions were produced, governed and protected.

*Derives from:* INT-0002

**source_ref**: Source Control System · **slsa_track**: Source
<!-- tl:end -->

<!-- tl:table type == 'system_requirement' and attrs.get('slsa_track') == 'Source' and attrs.get('slsa_group') == 'Source Control System' -->
| UID | Type | Status | Title |
|---|---|---|---|
| SR-0013 | system_requirement | approved | Repositories are uniquely identifiable |
| SR-0014 | system_requirement | approved | Revisions are immutable and uniquely identifiable |
| SR-0015 | system_requirement | approved | Human readable changes |
| SR-0016 | system_requirement | approved | Source Verification Summary Attestations |
| SR-0017 | system_requirement | approved | History |
| SR-0018 | system_requirement | approved | Continuity |
| SR-0019 | system_requirement | approved | Identity Management |
| SR-0020 | system_requirement | approved | Source Provenance |
| SR-0021 | system_requirement | approved | Protected Named References |
| SR-0022 | system_requirement | approved | Two-party review |
<!-- tl:end -->

