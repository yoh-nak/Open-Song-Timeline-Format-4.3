# Open Song Timeline Format — OSTF 4.3.0

**Formal written-specification release · 2026-11-16**

[日本語](README.ja.md) · [Complete manual](docs/COMPLETE_MANUAL.md) · [日本語マニュアル](docs/COMPLETE_MANUAL.ja.md) · [Parameter reference](docs/PARAMETER_REFERENCE.md) · [Examples](docs/EXAMPLES_GUIDE.md)

OSTF is a UTF-8 JSON format for portable song structure, harmony, notes, lyrics, MIDI expression and musical intent. It separates the authored **Score** from optional **Distributed Session** collaboration records and **Production Session** studio metadata. It is not a synthesizer, a DAW host, a plugin installer, a cloud service or a robot controller.

## Release scope

| Family | Serialized identity | Primary reference |
|---|---|---|
| Core Score | `format: "OSTF"`, `version: "4.3.0"` | [Core parameters](docs/PARAMETER_REFERENCE.md) |
| Distributed Session | `profile: "OSTF-Distributed-Session-0.2"` | [Session parameters](docs/SESSION_PARAMETER_REFERENCE.md) |
| Production Session | `profile: "OSTF-Production-Session"`, `profileVersion: "0.2.0"` | [Production parameters](docs/PRODUCTION_PARAMETER_REFERENCE.md) |

Core 4.3 retains the 4.2 data model and adds optional phrasing, vocal freedom, ensemble relationships, finite performance plans and musical performance requirements. The optional companions do not add network state, audio routing or plugin state to the Core Score.

## Start here

Open [01-minimal.ostf](examples/01-minimal.ostf) for the required song envelope, then [26-complete-authoring.ostf](examples/26-complete-authoring.ostf) for inherited and new optional parameters. [27-midi-mpe-complete.ostf](examples/27-midi-mpe-complete.ostf) covers both MPE zones. [28-legacy-preservation.ostf](examples/28-legacy-preservation.ostf) demonstrates retained legacy envelopes. Examples [29](examples/29-enumerated-alternatives-a.ostf) and [30](examples/30-enumerated-alternatives-b.ostf) provide mutually exclusive enum/status alternatives.

The [sample guide](docs/EXAMPLES_GUIDE.md) explains all 52 structured examples. A companion JSON file is not an OSTF song and must not be relabeled as one.

## Complete reference and sample coverage

| Family | Examples | Parameter declarations | Enum values | Positive union branches |
|---|---:|---:|---:|---:|
| Core | 30 `.ostf` | 646 / 646 | 263 / 263 | 37 / 37 |
| Distributed | 18 `.json` | 93 / 93 | 20 / 20 | 9 / 9 |
| Production | 4 `.json` | 103 / 103 | 45 / 45 | 7 / 7 |
| **Total** | **52** | **842 / 842** | **328 / 328** | **53 / 53** |

Every reachable named parameter declaration has a file/JSON-Pointer witness, including inherited legacy envelopes and conditional declarations. The full [coverage report](docs/COVERAGE_REPORT.md) defines the metric and links to machine-readable evidence. This is not an exhaustive test of infinite strings, numbers, custom extension keys, combinations, musical results or application behavior.

## Package contents

The release contains **100 files**, including this README, both complete manuals, the three parameter references, adopted specifications, four schemas (three active families plus the 4.2 baseline), examples, three synthetic assets, three local utilities, licenses, the publisher record, manifest and checksums. No separate download is required for the manuals or examples.

The nine adopted specification/schema files are intentionally retained byte-for-byte. Their development-era titles and approval notes are historical source text, **not the current release status**. [Edition and authority guide](docs/RELEASE_READINESS.md) explains the adopted precedence; [PUBLISHER_APPROVAL.json](PUBLISHER_APPROVAL.json) records the publisher instruction and source fingerprints. Public-facing manuals, references and release notes describe the final edition rather than the old approval workflow.

## Local inspection tools

```bash
python tools/verify_package.py
python -m pip install -r requirements.txt
python tools/verify_package.py --coverage
python tools/validate.py examples/26-complete-authoring.ostf
python tools/validate.py --session --pinned-ostf examples/22-pinned-session-aaba.ostf examples/session/03-snapshot-02.json
python tools/validate_production_profile.py examples/production/04-complete-production-02.json --score examples/22-pinned-session-aaba.ostf
```

The first command needs only Python's standard library. Schema/coverage and authoring checks use `jsonschema`. Tools are local, read-only aids, not complete independent implementations or certifications. No network, plugin or robot execution is performed.

## Publication and verification boundary

Publisher decisions D01–D05 were approved in the conversation that produced the source release. The current instruction authorizes this GitHub publication package. The record is **not a cryptographic signature or independent rights audit**. Runtime, independent-parser, DAW/plugin/DSP, Web/WAN, vocal-engine and physical-AI/robot hardware checks are excluded and are not claimed as passed.

Synthetic plugin-state BIN content is deliberately invalid and is never a loadable preset. All illustrated plugin identities are fictional. External Core Resource descriptors do not guarantee that the referenced bytes are bundled or available. Successful parsing does not prove a voicebank license, acoustic equivalence or product support.

## License

Specifications, schemas, documentation and example data: **CC0-1.0** ([LICENSE](LICENSE)). Python utilities: **MIT** ([LICENSE-CODE](LICENSE-CODE)). See [license policy](LICENSE-POLICY.md) and [notices](NOTICE.md). No rights to third-party plugins, presets, voicebanks or recordings are granted.

## GitHub publication

Extract the ZIP and publish its contents at the repository root. Use release tag **`v4.3.0`** and release title **`OSTF 4.3.0`**; use [RELEASE-NOTES.md](RELEASE-NOTES.md) for the release description. The ZIP is a distribution archive, not a standardized OSTF project-container format. Uploading and publishing the repository are separate actions and have not been performed by generating this package.
