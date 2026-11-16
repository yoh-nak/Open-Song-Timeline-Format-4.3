# OSTF 4.3.0 — 全網羅実装マニュアル

**正式公開版 · 2026年11月16日**

[English complete manual](COMPLETE_MANUAL.md) · [Core全項目](PARAMETER_REFERENCE.md) · [Distributed全項目](SESSION_PARAMETER_REFERENCE.md) · [Production全項目](PRODUCTION_PARAMETER_REFERENCE.md) · [サンプル案内](EXAMPLES_GUIDE.md)

## 1. このマニュアルの範囲

OSTF 4.3で扱う楽曲情報、4.2から継承したノート・MIDI・歌詞・歌唱表現、4.3の演奏意図、分散セッション、制作セッションを説明します。全フィールドの型・必須条件・数値範囲・列挙値・参照先は、3冊の全項目リファレンスに原Schemaとともに収録しています。英語版には継承Coreの詳細な実装章もまとめています。

「全網羅」は、定義されている項目・有限の選択肢・データ形状を説明し、サンプルの実体へたどれることを指します。無限の文字列や数値、自由な拡張キー、あらゆる音楽的組み合わせ、外部アプリケーションの挙動を保証する意味ではありません。

承認された規範正本の意味が最優先です。正本には承認前のDraft説明が残っていますが、正式採択後の優先関係は[版・権威ガイド](RELEASE_READINESS.md)に整理しています。本書から新たなJSONフィールドを追加することはありません。

## 2. 3種類の文書を混ぜない

| 文書 | データ内の識別 | 主な役割 |
|---|---|---|
| Core Score | `format="OSTF"`、`version="4.3.0"` | 楽曲構成、和声、ノート、歌詞、演奏意図 |
| Distributed Session | `profile="OSTF-Distributed-Session-0.2"` | 参加者、状態、提案・確定イベント、同期位置 |
| Production Session | `profile="OSTF-Production-Session"`、`profileVersion="0.2.0"` | ミキサー、デバイス、アセット、録音範囲、オートメーション |

Coreは`.ostf`、同梱のcompanionは`.json`です。拡張子の付け替えで互換性が生まれるわけではありません。ミキサーやネットワークの項目をCoreのルートへ勝手に混ぜないでください。

OSTFは音源、プラグインホスト、生成AI、ネットワークサービス、ロボット制御装置そのものではありません。意味を保存する形式と、その意味を実行するアプリケーションを分けます。

## 3. 最小文書とルート項目

[01-minimal.ostf](../examples/01-minimal.ostf)が最小の出発点です。必須ルートは`format`、`version`、`ppq`、`song`、`timeline`、`harmony`、`tracks`、`soundSlots`、`lyrics`、`resources`です。必要な配列が空でも、その形式の条件に従っていれば、無理に音符や歌詞を埋める必要はありません。

任意のルートには`drumKits`、`contributors`、`document`、`relativePhrases`、`generation`、`presentation`、`phraseLibrary`、`clipChoices`、`localization`、`provenance`、`midi`、`extensions`、`ensembleInteractions`、`performancePlans`があります。それぞれを以下の章で説明します。

`version`の文字列は厳密に扱います。4.2から4.3へ移す場合も、元のデータを確認し、必要な移行操作として版を変更します。新機能が任意であることは、未知データを削除してよいという意味ではありません。

## 4. JSON、文字コード、未知情報

UTF-8のJSONとして保存します。重複したメンバー名、NaN／Infinity、壊れた文字列や数値を、最初優先・最後優先で黙って修復しないでください。Schemaの構造判定と、ID参照や音楽上の意味の判定は別です。

知らない情報を表示できないことと、その情報を捨てて保存してよいことも別です。読み込み、表示、編集、保持、解釈、実行の対応状況を分けて表明します。旧形式の自由な情報は定義された拡張領域で保持しますが、現在のCoreに標準項目がある情報を新規作成時に拡張領域だけへ隠さないでください。

## 5. 時間、Tick、PPQ、半開区間

`ppq`は四分音符あたりのTick数です。整数で1〜960000を取ります。PPQ=960なら四分音符は960Tickです。小節数や秒数とは別の座標で、実時間はテンポマップに従って計算します。

範囲は`[start, start+duration)`の半開区間です。終端と次の始端が一致するだけで二重に含めないでください。Section、和声、Track Directionなどはグローバルなソース時間、Clipの開始位置もグローバル、NoteやMIDIイベントや歌唱イベントの指定項目はClipローカルです。

負のローカル開始位置が許される場面でも、絶対時刻が曲の先頭より前になることは許しません。イベント終端、Clip終端、ノートの発音区間の関係を確認します。テンポが途中で変わるときは、区間ごとにTickから時間へ積分し、一つのBPMで平坦化しないでください。

## 6. IDと参照、改訂の識別

Core内の新しいオブジェクトIDは適切な名前空間で一意にします。表示名や配列の並び順で対象を同定しないでください。`harmony.scales[].targets[].id`、`ref.id`、翻訳対象のIDは「新しいIDの宣言」ではなく「既存IDへの参照」です。両者を混同すると正しい文書まで重複IDとして拒否してしまいます。

`document.id`と`revisionId`は文書・改訂の識別です。親改訂、作成・変更ソフト、由来情報を記録できます。これらはCore内のNote IDとは同じ役割ではありません。SHA-256は元ファイルのバイト列の識別であり、署名や権利証明ではありません。

## 7. Song、クレジット、ジャンル、権利

`song`には題名、別題名、副題、説明、言語、ジャンル、ムード、キー、スケール、メロディ担当、主要歌詞文書、クレジット、権利の記述を入れます。ジャンル・ムードは開かれた記述であり、並び順を生成器の重みと決めつけません。

`contributors`が人物・組織等の識別情報を持ち、`song.credits`が役割を割り当てます。複数のクレジットが同じ貢献者を参照できます。`rights`の記述は、著作権や再配布権を外部で自動確認した証拠ではありません。多言語の題名を追加しても元の題名とIDを失わないようにします。

## 8. Timeline、Section、テンポ、拍子、キー変更

`timeline.sections`は開始と長さを持つ構成です。名前、role、翻訳名は表示情報と構成上の意味を持ちますが、別のタイムラインを作りません。`tempoChanges`、`meterChanges`、`keyChanges`、曲の長さ、`barOrigin`を別々に管理します。

拍子の分母や`beatGroups`はSchemaと意味規則に従います。キーは`tonal`、`atonal`、`unspecified`を区別します。調性がない／未指定のときに勝手にC majorを補わないでください。調性があるときは主音とmodeを明示し、未知のmodeをmajor/minorへ自動変換しません。

## 9. Chord、Bass、Voicing、Scale

`harmony.chords`がグローバルな範囲、コード名、ルート、インターバル、任意のスラッシュベース、ボイシングを持ちます。コード名と実際の保存ノートは別情報であり、コード解析でノートを書き換える操作は明示的な編集です。

ボイシングの`pitches`と対応する`velocities`を区別し、未指定を表す`null`もSchemaどおり保持します。ベロシティのない和声音列を、保存ノートの一律ベロシティへ変換しないでください。

`song.scale`は曲レベルの音集合、`harmony.scales`は時間範囲を持つスケール文脈です。Scaleの`targets`はSection、Track、Clip、Chord、Noteへの型付き参照です。即興で使う音集合の選択とは権威が異なり、Harmony Scaleが存在するだけで全Trackへ即興生成を命じるわけではありません。

## 10. Track、Instrument、Sound Source

TrackはID、名前、Clipの配列を持ちます。role、楽器名とfamily、演奏可能音域、enabled、表示優先、音源のヒントなどを追加できます。`trackType`の`melodic`、`drum`、`mixed`はイベント対象の意味であり、DAWのMIDI／Audio Trackのクラスそのものではありません。

`soundSource`は未割当、GM、外部MIDI、プラグイン、ホスト管理等の情報的なヒントです。プラグイン状態、ライセンス、物理MIDIポート、ロード命令ではありません。制作側の実際のデバイス並びはProduction側で別に扱います。

## 11. ClipとNote、ベロシティ、確率

Clipは曲上の位置と長さを持ち、NoteはClip内の開始位置と長さを持ちます。Noteの対象は`pitch`か`soundSlotId`のどちらか一つです。両方を同時に設定しません。

MIDI pitchは0〜127、発音ベロシティは1〜127、releaseVelocityは0〜127です。`enabled`、`probability`、`velocityDeviation`は別項目です。確率0のNoteと無効化されたNoteを同一情報に潰しません。velocityDeviationには元のvelocityが必要で、変化後も許容範囲内である必要があります。

`pitchRole="fixedTrigger"`はキー・スイッチ等の固定トリガーで、音楽的な移調や和声分析の材料にしません。Sound Slot型NoteにはpitchRoleを付けません。確率やベロシティ変動の乱数系列はOSTFが同一再現を標準化するものではありません。

## 12. Sound SlotとDrum Kit

Sound Slotは文書内の音色・イベント識別です。複数のSlotが同じMIDIノート番号に対応していても、同じイベントとして統合しません。`midiMapping`はGM1またはcustomを明示します。GM1の打楽器キー範囲などはSchemaの条件に従います。

Drum KitはSlotの集合を識別します。Trackが指定したキットの外のSlotを使わないように参照整合性を確認します。Slot名の言語、Track名、見た目からドラム種別を決定しません。

## 13. MIDI Bus、Channel、MPE

ルートの`midi.buses`は論理バスで、物理ポートや接続機器の指定ではありません。TrackのMIDIモードは`singleChannel`、`multiChannel`、`mpe`です。singleChannelはチャンネルを指定し、multiChannelはNote/Event側の具体的なチャンネルを扱います。モードごとに禁止・必須になるフィールドが異なります。

MPEはlowerまたはupperのzoneとmemberChannelCountを持ちます。lowerのマスターチャンネルは1、upperは16です。具体的なNoteとNote対象表現を、対象チャンネルとVoiceではなく正しいNote参照に関連付けます。[27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf)に上下両方のゾーンがあります。

## 14. MIDIイベント全種類

`controlChange`、`channelMode`、`programChange`、`pitchBend`、`channelPressure`、`polyPressure`を区別します。Note On／Offを別のMIDIイベントへ二重記録せず、具体ノートは`notes`に保存します。

Program Changeの保存値と機器画面の1始まりの表示値を混同しません。Pitch Bendの`value14`は0〜16383で中心は8192です。7bitへ丸めません。`targetNoteId`のあるイベントは参照先のNote・チャンネル・有効区間を確認します。同時刻の`order`は順序情報であり、曖昧な並びを配列順から勝手に確定しません。

MIDI CC 7/10/11などは音源へ渡る演奏情報です。ProductionのミキサーgainDb/panとは独立です。一方の編集を他方へ黙って転写しないでください。

## 15. Lyricsの文書、フレーズ、単位、割当

`lyrics.documents`が歌詞文書、`phrases`がまとまり、`units`が小単位、`alignments`がNoteとの関係です。表示する`text`、読みの`pronunciation`、音素候補の`phonetics`は別情報です。

一単位→一音、一単位→複数音、複数単位→一音、複数単位→複数音を表せます。ただし構造が有効でも、具体的な発音順序が未確定な場合があります。曖昧なmany-to-many関係を、変換器が黙って均等配分することはできません。

複数のmelodyTrackは複数の歌声を意味しません。楽器のメロディも有効です。歌唱へ渡すときは、次章のVoiceとAlignmentを明示的に解決します。

## 16. Lyric Voice、Vocal Profile、所有権

`lyrics.voices`はTrackとLyric Documentを関連付けます。異なるVoiceが同じ歌詞文書やソースNoteを参照できる場合もありますが、外部形式への複製・分割は書き出し結果の処理です。元のNoteを二つの正本へ増やしてはいけません。

`vocalProfile`はlanguage、deliveryMode（sing／rap／speak／hum）、声の説明を持つエンジン中立の情報です。商用声庫名やライセンスを推定するための権限ではありません。

Clipの`vocalPerformances`はVoiceに所属します。同じClipで同じVoiceの重複Performanceを作らず、VoiceのTrackを確認します。`noteIds`がある場合はそのClip内の実際の音高Noteを指し、そのVoiceの局所Alignmentが使用するNoteを含めます。なければ明示的なVoice付きAlignmentから所有範囲を解決し、melody roleから推測しません。

## 17. 音素、発音優先順位、同時刻順序

音素候補のalphabetはipa、xsampa、arpabet、otherです。otherにはnamespaceが必要です。symbolsは順序付きです。同じalphabetと言語の組でpreferred:trueを複数設けないようにします。異なる音素体系に一つずつpreferredを持たせることは区別して扱います。

明示的に時刻指定されたphonemeEvents、変換先へ写像できるphonetics、pronunciation、表示textからの辞書推定、という区別を保ちます。推定結果でソースを無断で書き換えません。同じVoice・Clip・開始Tickの音素にorderを付ける場合は、該当グループ全体の順序を一意にする必要があります。

外部歌唱形式への変換は、同梱されているという意味ではありません。SVP、USTX、VPR等を想定できても、アダプターの実装・読み戻し・実音確認は別の作業です。

## 18. 歌唱Pitch、Expression、Technique、Breath

歌唱pitchCurveは対象Noteの基準音高からのcents偏差です。MIDI pitch番号や生のPitch Bend値ではありません。pointsの時刻はClip相対です。同じVoice・Clip・Noteに複数の競合pitchCurveを作らず、点の重複時刻やNoteの範囲外を確認します。

expressionCurveはdynamics、breathiness、tension、brightness、voicingで、抽象的な0〜1の値です。省略は0.5などの既定値を意味しません。Note対象曲線は同じパラメーターのClip対象曲線と加算せず、定義された範囲で置き換えます。1点曲線と複数点曲線の範囲外の扱いを区別し、勝手な外挿をしません。

Techniqueはscoop、fall、vibrato、portamento、legato、staccato、accent、whisper、growl、falsetto、humming、rap、melismaの演奏意図です。具体曲線にすでに含まれる効果を二重適用しません。Breathはinhale／exhaleの時刻情報で、実際に可聴の息を合成するかは実装側です。

通常のMIDI再生ではMIDI層、歌唱書き出しでは明示的な歌唱層の対応する表現が権威を持ちます。両者を無条件で足してはいけません。

## 19. 相対フレーズ、生成情報、Groove

`relativePhrases`は、具体Noteとコード音／スケール度数の対応を記録します。具体Noteの代わりの第二の演奏正本ではありません。basis、contextId、anchorPitch、index、chromaticOffsetを揃えます。

`generation`は生成器、入力参照、出力参照、対象範囲、保護Note、生成意図を記録します。genreNames、moodNames、groove、prompt、seedは保存された文脈です。これらの文字列をプログラムやAIへの自動送信命令として実行しません。Grooveの単位TickとlongWeight／shortWeightを、保存ノートの時刻へ黙って再適用しないようにします。

`current`、`stale`、`unverified`は派生情報の状態です。元の和声やノートを編集したら、依存関係を確認して状態を更新します。未検証を成功と読み替えません。

## 20. Phrase Library、Clip Choices

Phrase Templateはソース音型、InstanceはClipへの具体的な対応、noteMapはTemplate Note・反復番号・実Noteの関係です。repeatCount、transpose、velocityMode、noteStateModeを区別します。Templateがあるだけで新しいNoteを発音するのではなく、保存済みのNoteと派生対応の関係を扱います。

Clip Choice Groupは候補と選択を持ちます。`selectedCandidateId=null`は候補未選択を表す許容形です。配列先頭を自動的に選択済みに変えたり、未選択候補を削除したりしません。

## 21. Presentation、Localization、Resources、Provenance

Presentationはrole定義、Sectionへのrole割当、標準role色、custom role色、個別オブジェクト色を持ちます。色は音楽的権威や再生順序を決めません。

Localizationは安定した対象IDとfieldに対して多言語値を保持します。表示名を変更しても参照IDは変更しません。旧形式のprofile-local ID参照と、現在のCore ID参照は区別してください。

Resourceはaudio／midi／text／otherの外部記述です。URIとhashが書かれているだけで実体が同梱されているとは限らず、ネットワーク取得の許可もありません。Provenanceはcreate、import、conversion、edit、transpose、merge、generation、other等の由来です。transposeのsemitonesやbeforeKey／afterKeyは履歴であり、現在のノートへもう一度移調を適用する指示ではありません。

## 22. 旧形式・第三者拡張の保持

`extensions`は定義された名前空間のenvelopeを保持します。旧relative-phrase、generation-context、appearance、legacy-import、phrase-library、clip-choices、localizationの形をリファレンスから省略していません。[28](../examples/28-legacy-preservation.ostf)に具体例があります。

これらは既存データを失わずに交換するためのもので、新規の標準情報を旧拡張にだけ保存することを推奨するものではありません。status、dependencies、version、dataの意味を保ち、未知dataを実行しません。Coreと旧拡張に同じ情報があってもCoreの正本を黙って置き換えません。

## 23. Track Directionの既存全種類

`improvisation`、`playingRole`、`pitchRange`、vendorの範囲型／時点型は4.3でも保持します。improvisationの音集合はeffectiveKeyScale、songScale、harmonyScales、explicitScaleを区別します。harmonyScalesには具体Scale参照、explicitScaleにはローカルな主音・intervalsを記録します。

playingRoleはその期間の役割、pitchRangeはstrict／preferredの音域です。vendorは名前空間、name、version、dataを持ち、範囲型と時点型を区別します。自然言語instructionは補助情報であり、構造化パラメーターを覆す実行命令ではありません。

## 24. 4.3 Phrasing

`type="phrasing"`はTrackに所属し、グローバルなstart／durationを持ちます。parametersにはadherenceが必須で、さらに少なくとも一つの音楽的項目が必要です。adherenceだけの空に近い指示は成立しません。

phraseLengthTicksとonsetGroupsPerQuarterはmin/max範囲で、min≤maxを確認します。同時刻の複数Note attackは一つのonset groupです。developmentはrepetition、motivicVariation、sequence、contrast、free。contourとenergyShapeもそれぞれ独立の有限列挙です。

motifRefはPhrase Templateへの参照です。energyShapeをベロシティや音量の直線へそのまま変換しないでください。strictも、読み込み時に保存Noteを無断で書き換える許可ではありません。

## 25. 4.3 Vocal Freedom

Voiceに対するtextPolicyとmelodyPolicyを独立に指定します。歌詞固定でも旋律は装飾可能であり、旋律固定でも歌詞がopenである場合があります。vocalizationKindはlexical、scat、humming、nonLexicalです。

textPolicy=alternativesのときだけcandidatePhraseSetsを記録し、異なる二つ以上の候補列を用意します。候補Phraseは同じVoiceの歌詞文書に属します。他のtextPolicyでcandidatePhraseSetsを残すことはできません。

これは生成・解釈の自由度の指定です。即座に新しいNote、歌詞、音素、声庫設定を作るものではありません。同じVoice・同種Directionの重複期間の扱いを確認し、配列の後勝ちで解決しません。

## 26. Ensemble InteractionとPerformance Requirement

Interactionはactorとpartnerの有向関係です。respondTo、followRhythm、alternateWith、leaveSpaceFor、reinforceを区別します。ソース範囲、Plan/Visit scope、または両方を持ち、両方なら共通部分に適用します。

同一Trackでの関係は、同じTrackに所属する異なる二つのVoiceを明示するときに限って扱います。自分自身への応答を暗黙に作りません。responseWindowTicksは音楽上の範囲で、WAN遅延や機械制御の制限ではありません。

TrackのperformanceRequirementsは必要同時発音数、音域、アーティキュレーション、最大onset密度です。演奏者のcapabilitiesとは別です。ロボットの可動域、力、停止命令、実機安全性の標準化は行いません。

## 27. Performance Plan、Visit、Part

Planは有限の演奏順序です。modeはorderedFinite、Visitは一つ以上、ordinalは重複のない0からの連番です。VisitはsourceSectionIdsかsourceRangeのどちらか一つを選びます。

PartはTrackとrealizationを指定します。fixedは保存された対象、openは開いた実現、silentはCoreの対象を鳴らさない選択です。Planで列挙しないTrackはdefaultRealizationに従います。unspecifiedがある計画を決定的な完全再現と宣伝してはいけません。

Visitのroleが元のplayingRoleと競合する場合は、同じTrackの対象DirectionをreplacesDirectionIdsで明示します。これで無関係な音域・歌唱・phrasing指示を消すことはできません。

## 28. 演奏時間への展開、連続と切断

ソースの位置、Clipローカル、展開後のperformanceTickを分けます。反復しても元NoteのIDや開始位置は書き換えず、各出現をPlan・Visit・セグメント・元Noteの組で識別します。実際に新しいCore Noteへ実体化するのは別の明示的な編集です。

ソース区間が連続するfixedの結合と、別位置へのジャンプや反復は同じではありません。連続条件を満たす発音ゲートはつながる場合がありますが、hard cutでは生き残る区間に従って切断し、ただ重なるという理由で新しいattackを捏造しません。

選択されたMIDIイベントと、選択された対象Noteの出現も別に解決します。Note対象の曲線はゲートへ追従し、Voice／Clip対象の表現を勝手に最寄りのNoteへ付け替えません。複数Noteへの歌詞Alignmentの一部しか選ばれないときに、歌詞全体が演奏されたとは扱いません。[時間展開](PERFORMANCE_TIMELINE.md)、[切断規則](NOTE_AND_MIDI_CUT_SEMANTICS.md)、[出現ID](SOURCE_OCCURRENCE_IDENTITIES.md)に詳細があります。

## 29. DistributedのScore固定と参加者

SnapshotとEventの両方がsessionId、documentId、revisionId、performancePlanId、scoreSha256を持ちます。元Scoreの実際のバイト列をhashし、整形・改行変更・BOM削除・JSON再シリアライズ後のバイトを代用しません。

参加者はTrack割当、対応機能、能力等を持ち、authorityParticipantIdを区別します。参加者の種別や能力が書かれていても、ネットワークや機械を操作する権限は生まれません。元Scoreの変更は既存Sessionの履歴を上書きするのではなく、新しいSession等の明示的な関連付けで扱います。

## 30. Distributedの全イベントと状態

| kind | 内容 |
|---|---|
| phraseProposed | 提案ID、対象Track、具体的なMIDIノートフレーズ |
| phraseCommitted | 権威側が採択した提案・対象・内容 |
| turnRequested | Trackの役割要求、任意のVisit指定 |
| cueIssued | cueId、任意の対象Visit |
| performanceObserved | 観測参加者、元Track、信頼度、特徴 |
| participantStatus | ready／busy／disconnected等の所定の状態と任意メッセージ |
| sessionStateChanged | 開始、停止、Visit変更、割当変更に応じたpayload |

prepared、playing、stoppedのライフサイクルと、baseStateRevision／resultStateRevisionを区別します。受理された状態更新は所定のrevision増分を満たす必要があります。重複eventId、同一内容の再送、異なる内容の衝突、権威のない更新を別々に扱います。

「提案」「採択」「実際に音が鳴った」は別です。状態確認やイベント受理だけで実演を証明しません。詳細は[状態機械](SESSION_STATE_MACHINE.md)です。

## 31. Distributedの位置、Clock、Late Join

PositionにはPlan/Visit、sourceTick、performanceTick、clockDomainId、epochUtc、uncertaintyMs等を記録します。ソースのテンポマップが音楽上の権威で、Sessionが勝手にテンポを上書きしません。Visit変更のanchor、時計領域、開始位置の整合を確認します。

midi1Notesの各NoteはphraseのdurationTicksの範囲内です。commitmentWindowは遅れて参加した実装に対して、どの範囲の確定情報を完全と主張するかを限定します。全履歴の完全性を自動的に証明するものではありません。

同梱の18件は複数シナリオの例です。ファイル名順に連結して、一つの正しいログとして再生することは想定していません。

## 32. ProductionのScore、Channel、ミキサー

Productionはscoreの元バイト列にsha256で関連付きます。ChannelのkindはScore Trackに結び付くtrack、制作側だけのaudioTrack、bus、masterです。Scoreに存在しない音声録音Trackを、架空のCore trackIdで結び付けません。

masterは一つで、出力、Send、Sidechainの参照と循環を確認します。gainDbはdB、panは-1〜1です。mute、solo、soloSafe、deviceIdsの順序を保存します。これらはMIDI CCやNote.enabledと別の権威です。

Soloはポータブルな対象選択の規則に従いますが、ホスト固有のpan law、エフェクト、実音までの同一性を保証しません。Solo操作で元Noteを削除することもありません。

## 33. Device、Plugin、Unavailable

Deviceはinstrument／effect／utilityの役割、plugin識別、enabled、bypass、任意のstateAssetId、未導入時の方針を持ちます。各ChannelのdeviceIdsが順序を決めます。

formatのvst2、vst3、au、aax、clap、builtin、hostNative、otherは識別形式であり、対応ソフトのバイナリや購入ライセンスではありません。namespace、pluginId、vendor、name、versionを無条件のロード命令にしないでください。

未導入時はreportAndPreserve、preserveAndSilence、preserveAndBypass等の所定の区別を保ちます。保持した設定で実際に復元・再生できたとは主張しません。同梱の識別子は架空です。

## 34. Asset、Audio Region、Frame

Assetには用途、URI、実バイトのhash、任意のメディア情報や長さがあります。音声sourceのsampleRateHz、frameCount、audioChannelsは音声フレームの座標で、曲のTickではありません。用途によって禁止されるメタデータもあります。

Regionは制作側Channel、sourceAsset、曲上の開始・長さ、元音声の開始Frame・Frame数、playbackMode、gain/mute、任意fadeを持ちます。nativeとfitを区別し、pitchPolicyも条件に従います。ファイル境界と曲上の境界をそれぞれ確認します。

元ファイルがないときに空の正常Assetとして扱いません。URIの保持と実バイトの保持、実バイトの保持と音響再現を分けます。相対パスの安全性、許可された取得範囲、明示的な再関連付けが必要です。

## 35. AutomationとSidechainの全対象

Automationのtargetは、channelのgainDb／pan／mute、deviceのparameterId、deviceControlのenabled／bypass、sendのgainDb／enabled、audioRegionのgainDb／muteです。MIDI CCへ置換しません。

点のatTickはソース時間で、時刻の重複・順序を確認します。Booleanはstep、数値は指定された補間を用います。プラグインパラメーターの数値は所定の正規化範囲で、異なるプラグイン間の音響同一性を意味しません。

SidechainはsourceChannel、targetDevice、入力port、pre/post FaderのtapPoint、followMute、gain、enabledを持つ検出信号の経路です。通常の可聴出力経路と分け、循環や不存在参照を確認します。ハードウェア入力へのアクセス許可は含みません。

## 36. ProductionとPlan、Host Extension、保持

Planの再進入では元のソースTickのRegion位相とAutomation値を参照します。単なる再生位置の履歴に依存して値を引き継ぐとは限りません。Coreのsilent指定を、制作側だけに存在する全オーディオ録音の自動muteとみなさないでください。

hostExtensionsはnamespacedな未知データを保持する領域です。読み込める、保持できる、編集できる、復元できる、同じ音で再生できる、を分けて表明します。

## 37. Score参照の解決順序

| 順序 | 条件 | 報告 |
|---|---|---|
| 1 | Companionの形式や必須pinが不正 | INVALID |
| 2 | 未対応の形式・版 | UNSUPPORTED |
| 3 | 許可された候補の列挙や必要な元バイト取得が未完了 | NOT_EVALUATED |
| 4 | 完了した範囲内に候補がない | MISSING |
| 5 | 候補はあるがhash一致なし | MISMATCH |
| 6 | 一致したScoreの構造が不正 | Score形式エラー |
| 7 | 必須のTrack／Plan／Visit／範囲等が未解決 | AMBIGUOUSと詳細理由 |
| 8 | 元バイトと必要参照がすべて一意に解決 | RESOLVED |

これは実装側の診断で、新しいJSON項目ではありません。一致する候補が一つ見つかっても、宣言した候補集合の必要な取得が未完了なら成功としません。失敗した候補を黙って除外せず、狭い範囲で再評価するなら新しい評価範囲として明示します。

ファイル名やURL、音楽的内容の一致だけでは元バイトの一致になりません。同じ元バイトのコピーが複数あることは、別のデータ同一性を増やしません。参照解決は実行権限、著作権、実音、実機安全性の証明ではありません。

## 38. 編集・保存・移行・書き出し

Clip移動ではグローバル位置とローカル時間を区別し、負のローカル時刻を再確認します。Note削除や移動では歌詞Alignment、Voice所属、曲線target、音素、Template対応、生成依存関係をまとめて確認します。IDを変更するなら参照も更新し、表示名での再検索に頼りません。

保存の整形だけでもバイト列は変わるため、旧hashで新しいScoreを指させません。Productionのrebindは明示的に関連付け直し、既存Distributed Sessionの元Scoreを暗黙に差し替えません。旧版参照を保持する場合には、その元バイトを取得できるかも区別します。

複数ファイルの保存失敗、結果不明、部分成功を一つの成功として表示しません。アプリケーションが保証する原子性や復旧方針を明示します。ダウングレードでは削除・近似・未対応を報告し、保存できたことを無損失や同一再生と読み替えません。

## 39. サンプルの読み方と全網羅性

01〜25は承認済みの元サンプルを保持しています。26は総合作成、27はMIDI/MPE、28は旧拡張保持、29/30は列挙値・null・状態の別形です。一つのオブジェクトに共存できない条件を、違法な全部入りファイルに押し込まず、複数の文書・オブジェクトで示しています。

Core646、Distributed93、Production103の宣言位置を合わせた842件、列挙値328件、正のoneOf/anyOf分岐53件に、それぞれ実ファイルとJSON Pointerの使用例があります。数値の境界を全通り試したり、全組み合わせを音楽として再生したりした意味ではありません。[対応表](COVERAGE_REPORT.json)から機械的にたどれます。

## 40. ローカルツールと正式公開

```bash
python tools/verify_package.py
python -m pip install -r requirements.txt
python tools/verify_package.py --coverage
python tools/validate.py examples/26-complete-authoring.ostf
python tools/validate.py --session --pinned-ostf examples/22-pinned-session-aaba.ostf examples/session/03-snapshot-02.json
python tools/validate_production_profile.py examples/production/04-complete-production-02.json --score examples/22-pinned-session-aaba.ostf
```

最初は標準ライブラリだけのファイル構成・hash照合です。coverageとSchema作成補助にはjsonschemaが必要です。補助チェッカーは全意味規則を独立に保証するものではありません。

配布ZIPは、文書・Schema・データ・素材・ライセンス・承認記録・ツールを含めて100ファイルです。ZIP自体を標準的なDAWプロジェクト形式と定義してはいません。

正式公開は発行者の承認に基づく文書規格としての公開です。動作、独立パーサー、DAW／プラグイン／DSP、歌唱エンジン、Web／WAN、フィジカルAI／ロボット実機の検証は条件から除外し、未実施です。これらを合格済みとは記載しません。CC0とMITの適用範囲、および他社素材の権利の限界はルートのライセンス方針を参照してください。
