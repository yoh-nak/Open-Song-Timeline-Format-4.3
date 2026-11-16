# OSTF 4.3.0 — Complete sample guide / 全サンプル案内

The suite contains **30 Core .ostf songs, 18 current Distributed .json records and 4 current Production .json profiles**. These are authored technical examples, not audio demonstrations or external application acceptance tests.

## Core Score — 30 files

| File | Purpose |
|---|---|
| [01-minimal.ostf](../examples/01-minimal.ostf) | Minimal required envelope / 必須ルートのみ |
| [02-guitar-solo.ostf](../examples/02-guitar-solo.ostf) | Guitar solo phrasing / ギターのフレージング |
| [03-jazz-comping.ostf](../examples/03-jazz-comping.ostf) | Jazz comping / ジャズの伴奏意図 |
| [04-aaba-performance-plan.ostf](../examples/04-aaba-performance-plan.ostf) | Finite AABA plan / 有限のAABA演奏順 |
| [05-rnb-vocal-open.ostf](../examples/05-rnb-vocal-open.ostf) | Open R&B vocal / 歌唱の自由度 |
| [06-scat.ostf](../examples/06-scat.ostf) | Scat intent / スキャット |
| [07-vocal-alternatives.ostf](../examples/07-vocal-alternatives.ostf) | Alternative lyric sequences / 歌詞候補 |
| [08-gospel-response.ostf](../examples/08-gospel-response.ostf) | Gospel response / 応答関係 |
| [09-techno-variation.ostf](../examples/09-techno-variation.ostf) | Techno variation / 反復変奏 |
| [10-physical-robot-requirements.ostf](../examples/10-physical-robot-requirements.ostf) | Musical requirements for physical performers / 必要演奏能力 |
| [11-harmony-plus-phrasing.ostf](../examples/11-harmony-plus-phrasing.ostf) | Harmony and phrasing / 和声とフレーズ |
| [12-visit-scoped-response.ostf](../examples/12-visit-scoped-response.ostf) | Visit-scoped response / Visitに限定した応答 |
| [13-fixed-notes-and-directions.ostf](../examples/13-fixed-notes-and-directions.ostf) | Fixed notes versus directions / 具体ノートの優先 |
| [14-tempo-map-reentry.ostf](../examples/14-tempo-map-reentry.ostf) | Tempo-map re-entry / テンポと再進入 |
| [15-vocal-response-phrasing.ostf](../examples/15-vocal-response-phrasing.ostf) | Vocal expression and phrase response / 歌唱表現と応答 |
| [16-inherited-comprehensive-core.ostf](../examples/16-inherited-comprehensive-core.ostf) | Inherited Core integration / 4.2継承の総合例 |
| [17-fixed-note-source-cut.ostf](../examples/17-fixed-note-source-cut.ostf) | Fixed-source note cuts / 音符の境界切断 |
| [18-visit-role-override.ostf](../examples/18-visit-role-override.ostf) | Visit role override / 一時的役割変更 |
| [19-concurrent-voice-directions.ostf](../examples/19-concurrent-voice-directions.ostf) | Concurrent voice directions / 複数Voice |
| [20-phrasing-with-motif-reference.ostf](../examples/20-phrasing-with-motif-reference.ostf) | Motif template reference / モチーフ参照 |
| [21-visit-and-range-intersection.ostf](../examples/21-visit-and-range-intersection.ostf) | Range/Visit intersection / 範囲とVisitの共通部分 |
| [22-pinned-session-aaba.ostf](../examples/22-pinned-session-aaba.ostf) | Pinned source for all Session/Production examples / 共通参照元 |
| [23-range-visit-and-label.ostf](../examples/23-range-visit-and-label.ostf) | Range, Visit and label / 範囲と表示名 |
| [24-intra-track-voices-response.ostf](../examples/24-intra-track-voices-response.ostf) | Same-track distinct-voice response / 同一Trackの異なるVoice |
| [25-source-note-repeated-visits.ostf](../examples/25-source-note-repeated-visits.ostf) | Repeated source-note visits / 同一ノートの反復出現 |
| [26-complete-authoring.ostf](../examples/26-complete-authoring.ostf) | Complete authoring catalogue / 全項目総合作成例 |
| [27-midi-mpe-complete.ostf](../examples/27-midi-mpe-complete.ostf) | Complete MIDI/MPE catalogue / MIDI全種と上下MPEゾーン |
| [28-legacy-preservation.ostf](../examples/28-legacy-preservation.ostf) | Legacy preservation catalogue / 旧拡張を保持する例 |
| [29-enumerated-alternatives-a.ostf](../examples/29-enumerated-alternatives-a.ostf) | All enumerated alternatives A / 列挙値・null・構造分岐 |
| [30-enumerated-alternatives-b.ostf](../examples/30-enumerated-alternatives-b.ostf) | Derived-status alternatives B / 派生データ状態の別選択 |

The full field catalogue spans several files because exclusive conditions cannot coexist in one object. Start with 01, then 26. The large alternatives catalogues 29/30 are technical shape witnesses rather than arrangements recommended for listening. Resources with URN/example paths may be descriptive external references with no bundled file.

## Distributed Session 0.2 — 18 files

All records pin the exact bytes of [22-pinned-session-aaba.ostf](../examples/22-pinned-session-aaba.ostf), its `documentId`, `revisionId` and finite Plan `form`. Do not reserialize that song without updating the binding deliberately.

| File | Scenario |
|---|---|
| [03-snapshot-02.json](../examples/session/03-snapshot-02.json) | snapshot: playing |
| [04-phrase-proposed-02.json](../examples/session/04-phrase-proposed-02.json) | event: phraseProposed —  |
| [05-phrase-committed-02.json](../examples/session/05-phrase-committed-02.json) | event: phraseCommitted —  |
| [06-snapshot-after-commit-02.json](../examples/session/06-snapshot-after-commit-02.json) | snapshot: playing |
| [07-session-state-change-02.json](../examples/session/07-session-state-change-02.json) | event: sessionStateChanged — visitChanged |
| [08-turn-request-02.json](../examples/session/08-turn-request-02.json) | event: turnRequested —  |
| [09-cue-issued-02.json](../examples/session/09-cue-issued-02.json) | event: cueIssued —  |
| [10-performance-observed-02.json](../examples/session/10-performance-observed-02.json) | event: performanceObserved —  |
| [11-participant-status-02.json](../examples/session/11-participant-status-02.json) | event: participantStatus — ready |
| [12-snapshot-prepared-02.json](../examples/session/12-snapshot-prepared-02.json) | snapshot: prepared |
| [13-snapshot-stopped-02.json](../examples/session/13-snapshot-stopped-02.json) | snapshot: stopped |
| [14-session-stopped-event-02.json](../examples/session/14-session-stopped-event-02.json) | event: sessionStateChanged — sessionStopped |
| [15-prepared-to-playing-event-02.json](../examples/session/15-prepared-to-playing-event-02.json) | event: sessionStateChanged — sessionStarted |
| [16-playing-after-start-02.json](../examples/session/16-playing-after-start-02.json) | snapshot: playing |
| [17-late-join-complete-window-02.json](../examples/session/17-late-join-complete-window-02.json) | snapshot: playing |
| [18-participant-busy-02.json](../examples/session/18-participant-busy-02.json) | event: participantStatus — busy |
| [19-participant-disconnected-02.json](../examples/session/19-participant-disconnected-02.json) | event: participantStatus — disconnected |
| [20-assignment-changed-02.json](../examples/session/20-assignment-changed-02.json) | event: sessionStateChanged — assignmentChanged |

The record files illustrate different scenarios and are **not one sequence to append in filename order**. In particular, busy/disconnected status and reassignment are separate examples. A state revision is accepted only by the designated authority under the adopted state-machine rules. Acceptance is not evidence of audible performance.

## Production Session 0.2.0 — 4 files

| File | Purpose |
|---|---|
| [01-track-mixer-plugin-chain.json](../examples/production/01-track-mixer-plugin-chain.json) | Mixer, devices, sends and automation / ミキサー・デバイス・センド |
| [02-unavailable-plugin.json](../examples/production/02-unavailable-plugin.json) | Unavailable instrument preservation / 未導入音源の保持 |
| [03-audio-regions-sidechain-02.json](../examples/production/03-audio-regions-sidechain-02.json) | Audio regions and sidechains / オーディオ範囲・サイドチェイン |
| [04-complete-production-02.json](../examples/production/04-complete-production-02.json) | Complete field/enum catalogue, host extensions, mono asset / 全項目・全選択肢 |

All four profiles bind the same source song 22. Plugin formats/IDs are illustrative and do not load real instruments. Examples 01/02 use 0.2.0 in this final distribution; their old source-package 0.1 envelopes are not the current files.

## Assets — 3 files

| Asset | Exact nature |
|---|---|
| [example-audio.wav](../examples/production/assets/example-audio.wav) | Synthetic 440 Hz tone; PCM16 stereo, 44.1 kHz, 11,025 frames |
| [mono-silence.wav](../examples/production/assets/mono-silence.wav) | Generated zero-valued PCM16 mono; 44.1 kHz, 11,025 frames |
| [example-plugin-state.bin](../examples/production/assets/example-plugin-state.bin) | 47-byte intentionally invalid plugin-state illustration; never a working preset |

The files are actual local bytes whose digests and byte lengths match the Production asset descriptors. This does not validate a decoder, plugin-state restore or audio output. `renderedAudio` is demonstrated as an asset-purpose descriptor, not evidence that a DAW rendered the tone.

## Coverage navigation

See [coverage report](COVERAGE_REPORT.md), [Core reference](PARAMETER_REFERENCE.md), [Session reference](SESSION_PARAMETER_REFERENCE.md), and [Production reference](PRODUCTION_PARAMETER_REFERENCE.md). Each definition table points to a sample and exact JSON Pointer.
