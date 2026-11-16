# OSTF 4.3.0 — Edition, adoption and authority / 版・採択・優先関係

## Current status

**Formal publisher-approved written-specification release, 2026-11-16.** D01 Core, D02 Distributed, D03 Production, D05 licensing policy and D04 publication were approved by the publisher instruction recorded in `PUBLISHER_APPROVAL.json`. The later packaging request authorizes this repository distribution. Approval of publication does not approve information loss in a user's future editing/export operation.

## Frozen adopted sources

The following nine files are retained with exactly the hashes in the prior approval record. No new normative field, requirement or interpretation was added while creating the manuals, references and examples.

| Adopted file | SHA-256 |
|---|---|
| `docs/SPECIFICATION.md` | `075a51db61239fa75cc27d8e402f67759bc852cbe0b8e196dcd9539fc2c8a145` |
| `docs/SPECIFICATION.ja.md` | `bc5b06e6edd413f1c11fd6bc513e73954005fead0aa82b9bd2f9cd96311f9989` |
| `schema/ostf-4.3.0.schema.json` | `72bf44666b42a760c883fbfa87e1da891467768032ee8e96fbee9fb47f673fc7` |
| `docs/SESSION_PROFILE.md` | `18196c82e9eeac97b79b639245637b89c43233671ddde834c6407a76d8b07dd2` |
| `docs/SESSION_PROFILE.ja.md` | `4b8e8f3f94eff07d24b3dc54dedca57051a365de3ce2020ea66d256b5405aa65` |
| `schema/ostf-distributed-session-0.2.schema.json` | `f79832adea0e48d6042c820a7d7a51e7a7288944bde833e255ce96c22b5ed0e7` |
| `docs/PRODUCTION_SESSION_PROFILE.md` | `42f12628afbcbdce72787b94675f5ba1e292ae7ccccae079cf1bc3c8174ba61b` |
| `docs/PRODUCTION_SESSION_PROFILE.ja.md` | `132ae206526eb92f4c042ce234bc702a95d7553ea51d4d603de8f6501594f023` |
| `schema/ostf-production-session-0.2.schema.json` | `1ac57129bfc1def9d5e1529b32d3905495c86e0d0b1f7530199a4dce72037e29` |

Their internal words “Draft”, “unratified”, “pending” and old D01–D05/NO-GO statements describe the **historical state when those source paragraphs were written**. They are not a second current publication decision. The first active reference-binding table in each adopted specification controls that topic; older conflicting tables are retained revision history, not additional simultaneous alternatives. This framing preserves the exact approved corpus instead of silently editing a document after it was approved.

## Precedence

The active family/version Schema defines serialized structure. Adopted normative prose defines cross-object meaning that JSON Schema cannot express. Inherited 4.2 musical authority is retained. Within the adopted corpus, the explicit active front-section binding decision and its stated supersession take precedence over historical conflicting binding examples. Manuals, parameter tables, sample witnesses, tools and packaging reports are explanatory aids and do not amend a field.

A 4.3 Core song uses `format="OSTF"`, `version="4.3.0"`. Distributed uses `profile="OSTF-Distributed-Session-0.2"`; Production uses `profile="OSTF-Production-Session"` and `profileVersion="0.2.0"`. Historical 0.1 files are not aliases and are not shipped here. The baseline 4.2 Schema is included only for compatibility inspection; 4.3 examples are authored against the 4.3 Schema.

## Reading path

Use the complete manuals and parameter references for normal implementation work. Consult the adopted specifications for normative wording and historical precedence. Read `SEMANTIC_RULES.md` and the focused time/cut/session notes for cross-object details; old approval language in those supporting notes is likewise historical. Runtime claims are never created by adoption or by a passing local check.

## 日本語

このパッケージは正式公開版です。正本6文書と現行Schema3件は、一括承認されたファイルをそのまま保持しています。内部のDraft番号や承認待ちの記述は、作成当時の履歴です。現在の承認状態は同梱承認記録に基づきます。過去の参照判定表を現行表と同時に適用することはしません。

通常の実装では正式版マニュアル→全項目リファレンス→サンプル対応表の順で参照してください。意味規則に疑問がある場合は採択正本の現行規則を優先します。これらは音響再現や外部製品の対応を保証せず、将来の編集・書出での情報損失を一括許可するものでもありません。
