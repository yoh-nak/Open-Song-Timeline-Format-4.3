# Open Song Timeline Format — OSTF 4.3.0

**正式な文書規格リリース · 2026年11月16日**

[English](README.md) · [全網羅マニュアル](docs/COMPLETE_MANUAL.ja.md) · [英語版マニュアル](docs/COMPLETE_MANUAL.md) · [全項目リファレンス](docs/PARAMETER_REFERENCE.md) · [全サンプル案内](docs/EXAMPLES_GUIDE.md)

OSTFは、楽曲構成、コード、スケール、ノート、歌詞、MIDI表現、演奏意図をUTF-8のJSONで交換するための形式です。楽曲の正本である **Score**、遠隔参加者の状態を扱う **Distributed Session**、ミキサーやプラグイン設定を扱う **Production Session** を分けています。

OSTF自体が音を合成したり、DAWやプラグインを起動したり、AIサービスへ接続したり、ロボットを動かしたりするわけではありません。

## 収録仕様

| 系統 | データ内の識別情報 | リファレンス |
|---|---|---|
| 楽曲・Core 4.3 | `format: "OSTF"`、`version: "4.3.0"` | [Core全項目](docs/PARAMETER_REFERENCE.md) |
| Distributed Session 0.2 | `profile: "OSTF-Distributed-Session-0.2"` | [分散セッション全項目](docs/SESSION_PARAMETER_REFERENCE.md) |
| Production Session 0.2.0 | `profile: "OSTF-Production-Session"`、`profileVersion: "0.2.0"` | [制作セッション全項目](docs/PRODUCTION_PARAMETER_REFERENCE.md) |

4.3では4.2のCoreを継承し、フレージング、歌詞と旋律の自由度、アンサンブルの関係、有限の演奏順序、必要な演奏能力を任意情報として追加しています。単純な楽曲にこれらを強制することはありません。

## 読み始める順序

[日本語マニュアル](docs/COMPLETE_MANUAL.ja.md)で全体像を確認し、[最小サンプル](examples/01-minimal.ostf)を開いてください。[総合作成例](examples/26-complete-authoring.ostf)に歌詞・歌唱表現・生成情報・演奏意図などをまとめています。[MIDI/MPE例](examples/27-midi-mpe-complete.ostf)、[旧形式保持例](examples/28-legacy-preservation.ostf)、[選択肢例A](examples/29-enumerated-alternatives-a.ostf)、[選択肢例B](examples/30-enumerated-alternatives-b.ostf)を併せて全項目を参照できます。

## 全網羅の対象

| 系統 | サンプル数 | 項目宣言 | 列挙値 | 構造分岐 |
|---|---:|---:|---:|---:|
| Core | `.ostf` 30件 | 646 / 646 | 263 / 263 | 37 / 37 |
| Distributed | `.json` 18件 | 93 / 93 | 20 / 20 | 9 / 9 |
| Production | `.json` 4件 | 103 / 103 | 45 / 45 | 7 / 7 |
| **合計** | **52件** | **842 / 842** | **328 / 328** | **53 / 53** |

ここでいう項目数はSchemaの宣言位置の数で、条件付き定義や同名の別定義を含みます。各項目にサンプルファイルとJSON Pointerを対応付けています。任意の文字列、無限の数値、自由な拡張キー、全組み合わせ、全ジャンルの音楽や音響結果までを網羅したという意味ではありません。詳細は[網羅性レポート](docs/COVERAGE_REPORT.md)と[機械可読の対応表](docs/COVERAGE_REPORT.json)に記録しています。

Distributed／Productionは楽曲本体ではないため、正しい形式として`.json`で収録しています。拡張子だけを`.ostf`へ変えて読み込ませることは想定していません。

## 100ファイル以内の正式配布物

ZIPの中は**合計100ファイル**です。マニュアル、リファレンス、規範仕様、Schema、サンプル、素材、ツール、ライセンス、承認記録、チェックサムをすべて含みます。開発途中の承認台帳や不正データの試験用ファイルを公開用パッケージから整理しました。

承認対象の規範文書6件・Schema3件は、承認済みのバイト列を保持しています。その正本に残るDraft番号や未承認時の記録は、採択に至るまでの履歴であり、現在の公開状態ではありません。正式な採択範囲と優先関係は[版・権威ガイド](docs/RELEASE_READINESS.md)、発行者の承認は[PUBLISHER_APPROVAL.json](PUBLISHER_APPROVAL.json)を参照してください。公開用マニュアルとリファレンスは正式版の案内として再構成しています。

## 静的な確認ツール

```bash
python tools/verify_package.py
python -m pip install -r requirements.txt
python tools/verify_package.py --coverage
python tools/validate.py examples/26-complete-authoring.ostf
```

最初のコマンドはPython標準機能だけでファイル数とハッシュを確認します。`--coverage`と作成補助チェッカーには`jsonschema`が必要です。これらはローカルの内容照合であり、全意味規則の独立検証や実際の演奏・音響処理の合格を示すものではありません。

## 公開判定と未実施の検証

D01〜D05は発行者の明示的な一括承認を記録しています。今回の依頼に基づき、GitHubで公開する配布物としてまとめ直しました。承認記録は暗号署名でも第三者による権利監査でもありません。

動作、独立パーサー、DAW／プラグイン／DSP、Web／WAN、歌唱エンジン、フィジカルAI／ロボット実機の検証は、公開条件から除外しています。未実施のものを実施・合格済みとは扱いません。

プラグインIDは架空の記述例です。BINは意図的に有効なプリセットではないダミーです。外部Resourceの記述は、その実体ファイルの同梱や利用可能性を保証しません。

## ライセンスとGitHubへの公開

仕様・Schema・文書・サンプルデータは**CC0-1.0**、Pythonツールは**MIT**です。[適用方針](LICENSE-POLICY.md)と[NOTICE](NOTICE.md)を同梱しています。他社製プラグイン、音源、プリセット、歌声ライブラリの権利を許諾するものではありません。

ZIPを展開し、中身をリポジトリ直下へ配置してください。リリースタグは **`v4.3.0`**、リリース名は **`OSTF 4.3.0`**、説明には[RELEASE-NOTES.md](RELEASE-NOTES.md)を使用できます。GitHubへのアップロードそのものは、このファイル生成では実施していません。
