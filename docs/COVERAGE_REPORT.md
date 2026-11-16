# OSTF 4.3.0 — Coverage report / 網羅性の対応表

Release: 2026-11-16. This is an authoring-time **static content inventory**, not independent interoperability certification.

## Measured coverage / 確認範囲

| Family | Sample files | Parameter declarations | Enum literals | Positive union branches |
|---|---:|---:|---:|---:|
| core | 30 | 646 / 646 | 263 / 263 | 37 / 37 |
| session | 18 | 93 / 93 | 20 / 20 | 9 / 9 |
| production | 4 | 103 / 103 | 45 / 45 | 7 / 7 |

**Total: 842 / 842 parameter declaration sites, 328 / 328 enum literals, 53 / 53 positive union branches.**

項目数はSchemaの宣言位置を数えています。同じ名前が別の定義や条件付き制約に現れる場合は別件です。無限の文字列・数値・配列長、任意の拡張キー、全ての値の組み合わせ、全ジャンルの演奏結果を網羅したという意味ではありません。`if`や`not`の判定条件そのものは、別の入力パラメーターとして数えません。

`COVERAGE_REPORT.json` contains the exact Schema pointer, sample file, and JSON Pointer for every covered item and enum value. An enum example is counted only against the corresponding applicable definition. Examples were parsed and compared with their supplied versioned schemas as an editorial construction check. This does **not** claim a fully independent semantic audit, DAW playback, voice synthesis, plugin restoration, WAN execution or robot operation.

## Why multiple files are necessary / 複数サンプルに分ける理由

A pitch Note and a Sound Slot Note are exclusive target shapes. A Visit selects `sourceSectionIds` **or** `sourceRange`, never both. `candidatePhraseSets` is required only when `textPolicy=alternatives`. MPE, multi-channel and single-channel routing have distinct conditional fields. Several derived-data statuses cannot be held simultaneously by the same object. The corpus therefore covers alternatives across separate objects/documents rather than making an invalid “everything in one object” file.

`.ostf` is reserved here for Core Score examples. Distributed and Production companions keep `.json` and their own discriminators. Renaming a companion to `.ostf` does not turn it into an OSTF song.

## How to locate a field / 探し方

1. Open the relevant parameter reference and search for the JSON property name or `$defs` name.
2. Follow the sample link beside that field.
3. Use the shown JSON Pointer to locate the exact data object. Array indices are zero-based.

The package includes 30 Core songs, 18 Distributed Session records, and 4 Production Session documents. Some events are independent scenarios, not one append-only event log. All plugin identities are illustrative; the binary state is deliberately nonfunctional. Core Resource URIs can be descriptors for external material that is not shipped. See [sample guide](EXAMPLES_GUIDE.md).

## Scope boundaries / 判定しない事項

No runtime, independent-parser, DAW/plugin/DSP, Web/WAN, physical-AI or robot hardware test is a release condition, and none is represented as passed. File hashes demonstrate byte identity only. Coverage demonstrates the presence of serialized examples only. Neither demonstrates ownership of third-party assets, sound equivalence, musical quality or complete application support.

## Release assembly checks / 公開パッケージの静的照合

The assembled repository contains **100 files**, including **52 structured examples** and **3 local illustrative assets**. The nine adopted normative files retain their approved hashes. All 1,014 relative Markdown file links resolve, and all 660 inspected local Markdown anchor links resolve. The 30 Core and 18 Distributed examples passed the bundled selected authoring checks; all 4 Production documents passed the bundled selected schema/reference/asset checks. These are content-construction checks, not independent implementation or runtime tests.

`PACKAGE_MANIFEST.json` identifies 98 content files; `SHA256SUMS.txt` identifies those files plus the manifest, for 99 checksums. Neither hash list attempts to contain its own digest. The final ZIP digest is supplied outside the archive. `python tools/verify_package.py --coverage` reproduces package integrity, schema acceptance and the measured coverage.
