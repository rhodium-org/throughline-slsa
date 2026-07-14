"""SLSA v1.2 spec content, transcribed for the throughline source generator.

Structure: two normative *tracks* (Build, Source), each with a root intent; every track
groups its requirements (Producer / Provenance generation / Isolation strength for Build;
Organization / Source Control System for Source); every requirement carries the minimum
level at which it becomes mandatory. Source is authoritative at https://slsa.dev/spec/v1.2/
(SLSA is an OpenSSF / Linux Foundation project, CC BY 4.0).

Requirement `text` re-expresses each MUST statement testably; `rationale` captures the
threat/why the spec gives for it.
"""

EDITION = "1.2"

TRACKS = [
    {
        "track": "Build",
        "intent_uid": "INT-0001",
        "title": "Software artifacts are built with verifiable integrity and provenance",
        "text": (
            "The SLSA Build track exists so that a software artifact is produced by a build "
            "process whose integrity and provenance can be verified against graded levels "
            "(Build L0 through L3). Higher levels move from provenance merely existing, "
            "through provenance signed by a hosted platform, to hardened builds whose "
            "provenance is strongly resistant to forgery — giving consumers a graded basis "
            "for trusting how an artifact was produced rather than ad-hoc judgement."
        ),
        "source_ref": "Build track",
        "groups": [
            {
                "source_ref": "Producer",
                "title": "Producer",
                "text": (
                    "Requirements on the producer — the organization that owns and releases "
                    "the software — to choose a capable build platform, build consistently, "
                    "and distribute provenance to consumers."
                ),
                "requirements": [
                    {
                        "source_ref": "Choose an appropriate build platform",
                        "title": "Choose an appropriate build platform",
                        "text": (
                            "The producer selects a build platform that is capable of "
                            "reaching their desired SLSA Build level."
                        ),
                        "rationale": (
                            "A producer can only achieve a given level of assurance if the "
                            "platform they build on is itself capable of meeting that level's "
                            "requirements."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Follow a consistent build process",
                        "title": "Follow a consistent build process",
                        "text": (
                            "The producer builds their artifact in a consistent manner, such "
                            "that verifiers can form expectations about the build process."
                        ),
                        "rationale": (
                            "Consistency lets verifiers establish what a legitimate build "
                            "looks like and detect deviations from it."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Distribute provenance",
                        "title": "Distribute provenance",
                        "text": (
                            "The producer distributes provenance to artifact consumers."
                        ),
                        "rationale": (
                            "Consumers can only verify an artifact's integrity and origin if "
                            "the provenance describing how it was built reaches them."
                        ),
                        "level": 1,
                    },
                ],
            },
            {
                "source_ref": "Provenance generation",
                "title": "Provenance generation",
                "text": (
                    "Requirements on the build platform to generate provenance that describes "
                    "how a package was produced, and to make that provenance authentic and "
                    "then unforgeable as the Build level rises."
                ),
                "requirements": [
                    {
                        "source_ref": "Provenance exists",
                        "title": "Provenance exists",
                        "text": (
                            "The build process generates provenance that unambiguously "
                            "identifies the output package by cryptographic digest and "
                            "describes how that package was produced."
                        ),
                        "rationale": (
                            "Provenance that names the exact artifact and its build lets "
                            "consumers detect mistakes and enables the stronger checks that "
                            "higher levels add."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Provenance is authentic",
                        "title": "Provenance is authentic",
                        "text": (
                            "Consumers can validate the authenticity of the provenance "
                            "attestation through a digital signature from a private key "
                            "accessible only to the build platform."
                        ),
                        "rationale": (
                            "A signature bound to the build platform lets consumers confirm "
                            "the provenance was issued by the real builder and was not altered "
                            "in transit."
                        ),
                        "level": 2,
                    },
                    {
                        "source_ref": "Provenance is unforgeable",
                        "title": "Provenance is unforgeable",
                        "text": (
                            "Provenance is strongly resistant to forgery by tenants; secret "
                            "material used to sign it is stored in secure systems and is not "
                            "accessible to user-defined build steps."
                        ),
                        "rationale": (
                            "If a tenant's own build steps could reach the signing key, they "
                            "could forge provenance for a package they did not legitimately "
                            "build."
                        ),
                        "level": 3,
                    },
                ],
            },
            {
                "source_ref": "Isolation strength",
                "title": "Isolation strength",
                "text": (
                    "Requirements on the build platform to run builds on hosted "
                    "infrastructure and, at higher levels, in an isolated environment free of "
                    "unintended external influence."
                ),
                "requirements": [
                    {
                        "source_ref": "Hosted",
                        "title": "Hosted",
                        "text": (
                            "All build steps ran using a hosted build platform on shared or "
                            "dedicated infrastructure, not on an individual's workstation."
                        ),
                        "rationale": (
                            "A managed, hosted platform provides security controls and "
                            "auditability that an individual developer machine cannot."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Isolated",
                        "title": "Isolated",
                        "text": (
                            "The build platform ensured that build steps ran in an isolated "
                            "environment, free of unintended external influence."
                        ),
                        "rationale": (
                            "Isolation prevents one build from tampering with another, "
                            "poisoning shared caches, or reaching signing credentials."
                        ),
                        "level": 3,
                    },
                ],
            },
        ],
    },
    {
        "track": "Source",
        "intent_uid": "INT-0002",
        "title": "Source revisions have verifiable authorship, history and provenance",
        "text": (
            "The SLSA Source track exists so that the authoring, review and management of "
            "source code can be verified against graded levels (Source L1 through L4). "
            "Higher levels move from source merely being version-controlled, through "
            "continuous, attested history and provenance, to continuously enforced technical "
            "controls and two-party review — giving consumers a graded basis for trusting how "
            "a source revision was produced, everything that happens before a revision reaches "
            "a builder."
        ),
        "source_ref": "Source track",
        "groups": [
            {
                "source_ref": "Organization",
                "title": "Organization",
                "text": (
                    "Requirements on the organization that produces source revisions — to "
                    "choose a capable source control system, control access and enforce "
                    "history, and (at higher levels) continuously enforce technical controls."
                ),
                "requirements": [
                    {
                        "source_ref": "Choose an appropriate source control system",
                        "title": "Choose an appropriate source control system",
                        "text": (
                            "The organization producing source revisions selects a source "
                            "control system (SCS) that is capable of reaching their desired "
                            "SLSA Source level."
                        ),
                        "rationale": (
                            "The source level an organization can reach is bounded by the "
                            "capabilities of the SCS they choose."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Configure the SCS to control access and enforce history",
                        "title": "Configure the SCS to control access and enforce history",
                        "text": (
                            "The organization configures access controls, using the "
                            "SCS-provided identity management, to restrict sensitive "
                            "operations on the repository; configures the SCS to produce a "
                            "reliable change history for its consumable revisions; and, where "
                            "tags exist, prevents them from being moved or deleted."
                        ),
                        "rationale": (
                            "Access controls and an immutable history are the foundation for "
                            "trusting who changed the source and what changed."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Safe expunging process",
                        "title": "Safe expunging process",
                        "text": (
                            "Where the SCS allows content to be expunged from a repository and "
                            "its history without a public record, the organization only does "
                            "so to meet legal or privacy compliance requirements, documents "
                            "the process and its tracking, and requires an administrator plus "
                            "at least one other trusted person to trigger it."
                        ),
                        "rationale": (
                            "Removing content without a record can break downstream integrity, "
                            "so it is constrained to compliance needs and gated by more than "
                            "one person."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Continuous technical controls",
                        "title": "Continuous technical controls",
                        "text": (
                            "The organization provides evidence of continuous enforcement, via "
                            "technical controls, for any claims made in Source Provenance "
                            "attestations or VSAs, and documents the meaning of those controls."
                        ),
                        "rationale": (
                            "A claim about how revisions are produced is only credible if the "
                            "control behind it is enforced continuously and its meaning is "
                            "written down."
                        ),
                        "level": 3,
                    },
                ],
            },
            {
                "source_ref": "Source Control System",
                "title": "Source Control System",
                "text": (
                    "Requirements on the source control system (SCS) — to make repositories "
                    "and revisions identifiable and immutable, expose human-readable changes, "
                    "and issue verifiable attestations about how revisions were produced, "
                    "governed and protected."
                ),
                "requirements": [
                    {
                        "source_ref": "Repositories are uniquely identifiable",
                        "title": "Repositories are uniquely identifiable",
                        "text": (
                            "The SCS defines a repository ID that is uniquely identifiable "
                            "within the SCS via a stable locator, such as a URI."
                        ),
                        "rationale": (
                            "A stable, unique repository identifier lets attestations and "
                            "consumers refer to exactly one source repository."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Revisions are immutable and uniquely identifiable",
                        "title": "Revisions are immutable and uniquely identifiable",
                        "text": (
                            "The SCS defines a revision ID that is uniquely identifiable within "
                            "the repository; where the revision ID is not a content digest, the "
                            "SCS documents how the revision's immutability is established."
                        ),
                        "rationale": (
                            "An immutable, unique revision identifier guarantees that a "
                            "reference always resolves to identical source content."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Human readable changes",
                        "title": "Human readable changes",
                        "text": (
                            "The SCS provides tooling to display the changes between one source "
                            "revision and another in human-readable form for all plain-text "
                            "changes, and where possible for non-plain-text changes."
                        ),
                        "rationale": (
                            "Reviewers can only judge whether a change is appropriate if they "
                            "can see what actually changed."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "Source Verification Summary Attestations",
                        "title": "Source Verification Summary Attestations",
                        "text": (
                            "The SCS generates a Source Verification Summary Attestation (VSA) "
                            "indicating the SLSA Source level of any revision at Level 1 or "
                            "above, and makes it fetchable by any consumer authorized to access "
                            "the revision."
                        ),
                        "rationale": (
                            "A VSA communicates a revision's source level to consumers in a "
                            "standard, verifiable form; absence of a VSA means Source Level 0."
                        ),
                        "level": 1,
                    },
                    {
                        "source_ref": "History",
                        "title": "History",
                        "text": (
                            "The SCS records all changes to named references — when they "
                            "occurred, who made them, and the new revision ID — and, where "
                            "revisions have ancestry, only allows a branch to advance to "
                            "revisions that descend from its current revision."
                        ),
                        "rationale": (
                            "A complete, append-only history enables audit and prevents "
                            "unauthorized rewrites of a branch."
                        ),
                        "level": 2,
                    },
                    {
                        "source_ref": "Continuity",
                        "title": "Continuity",
                        "text": (
                            "For each technical control claimed in a VSA, the SCS establishes "
                            "and tracks continuity from a specific start revision, "
                            "re-establishing it from a new revision after any lapse, with "
                            "exceptions only via the safe expunging process."
                        ),
                        "rationale": (
                            "Continuity demonstrates that a claimed control has been enforced "
                            "without gaps, not just at a single point in time."
                        ),
                        "level": 2,
                    },
                    {
                        "source_ref": "Identity Management",
                        "title": "Identity Management",
                        "text": (
                            "The SCS provides an identity management system to identify and "
                            "authenticate actors, lets organizations specify which actors and "
                            "roles may perform sensitive actions, and attributes activity to "
                            "authenticated identities."
                        ),
                        "rationale": (
                            "Attributing actions to authenticated identities is what makes "
                            "accountability and role-based policy enforcement possible."
                        ),
                        "level": 2,
                    },
                    {
                        "source_ref": "Source Provenance",
                        "title": "Source Provenance",
                        "text": (
                            "The SCS creates Source Provenance contemporaneously with each "
                            "branch update, providing a credible, auditable record of changes, "
                            "and makes it accessible to any consumer authorized to access the "
                            "revision."
                        ),
                        "rationale": (
                            "Provenance created at the moment of change is tamper-resistant "
                            "evidence of how a revision came to be."
                        ),
                        "level": 2,
                    },
                    {
                        "source_ref": "Protected Named References",
                        "title": "Protected Named References",
                        "text": (
                            "The SCS lets an organization enforce customized technical controls "
                            "for named references, indicate which references are protected, and "
                            "records the controls enforced on them in contemporaneously "
                            "produced attestations associated with the corresponding revisions."
                        ),
                        "rationale": (
                            "Marking branches as protected and recording the controls enforced "
                            "on them produces the evidence higher-level consumers rely on."
                        ),
                        "level": 3,
                    },
                    {
                        "source_ref": "Two-party review",
                        "title": "Two-party review",
                        "text": (
                            "Changes to protected branches are agreed to by two or more trusted "
                            "persons before submission, with review covering at least "
                            "security-relevant properties, applied to the final submitted "
                            "revision; the SCS presents reviewers with a clear representation of "
                            "the change being accepted."
                        ),
                        "rationale": (
                            "Requiring a second trusted person prevents any single actor from "
                            "unilaterally introducing a malicious change."
                        ),
                        "level": 4,
                    },
                ],
            },
        ],
    },
]
