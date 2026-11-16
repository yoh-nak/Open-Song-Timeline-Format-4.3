# OSTF 4.3.0

Formal written-specification release, 2026-11-16. Tag: `v4.3.0`.

## Highlights

OSTF 4.3 retains the 4.2 Core and adds optional Phrasing and Vocal Freedom Directions, Ensemble Interactions, finite Performance Plans, and musical Performance Requirements. Distributed Session 0.2 and Production Session 0.2.0 remain separate optional companions.

This GitHub distribution provides complete English/Japanese manuals, schema-derived parameter references, **30 Core .ostf songs**, **18 Distributed JSON records**, **4 Production JSON documents**, three synthetic assets, four schemas, local authoring tools, publisher authorization and checksums within **100 files**.

## Coverage

The example corpus supplies witnesses for **842/842 reachable parameter declarations**, **328/328 enum literals**, and **53/53 positive oneOf/anyOf branches** across the three active schema families. Every witness is recorded with a file and JSON Pointer. Conditional duplicates are counted by Schema declaration site; arbitrary values and combinations are not claimed exhaustive.

New examples cover optional inherited metadata, harmony targets and voicing, lyrics and vocal expression, both MPE zones and all MIDI event types, legacy envelopes, nullable alternatives, all enumerated policies, session status/assignment events, plugin-format descriptors, host extensions and mono/stereo assets.

## Publication cleanup

The adopted nine-file normative corpus remains byte-identical to the publisher-approved source. The final manuals, references, example guide, README and release information replace development approval workflow as the main reading path. Historical Profile 0.1 examples/schemas and negative test fixtures are not included in this current-release distribution. Production examples 01/02 now explicitly use Profile 0.2.0.

The local Core authoring checker now distinguishes harmony-scale target references from ID declarations. New tooling inspects manifest/checksum integrity and reproduces the static coverage counts. It is not a complete independent validator.

## Important boundary

Publisher approval permits this written-specification release within the publisher's authority. Runtime, independent-parser, DAW/plugin/DSP, vocal-engine, Web/WAN and physical-AI/robot hardware verification are excluded and are not claimed as passed. All plugin identities are illustrative. The BIN is deliberately invalid plugin-state data, not a preset. No acoustic equivalence, vendor-format conversion or third-party product support is certified.

## License

CC0-1.0: specification, schema, documentation and example data. MIT: Python utilities. No proprietary plugin, voicebank, preset or recording rights are granted.

---

## 日本語概要

OSTF 4.3.0の正式公開用パッケージです。Coreの音楽データと演奏意図、遠隔セッション、制作セッションを分離したまま、全項目のマニュアル・リファレンス・サンプルを100ファイル以内に収録しました。

承認済み規範仕様の意味やSchema構造は変更していません。全網羅は有限の項目宣言・列挙値・構造分岐に対するサンプル収録を指し、実行環境の互換性保証を意味しません。実動作等の検証は公開条件から除外し、未実施のままであることを明記しています。
