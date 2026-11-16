# OSTF 4.3.0 — Notices and provenance

This distribution is based on `OSTF_4.3.0_Publisher_Approved_Specification.zip`, SHA-256 `1440d16a440ba26d679bf940fe4fc8a68c5ad86c9944c6e35471bbbc7fdd6351`. The publisher approved the written specification and its licensing policy in the originating conversation. The subsequent request authorized GitHub publication packaging with comprehensive documentation and examples within 100 files.

The nine adopted specification/schema files are preserved exactly. Their dated Draft notes are historical. Current release identity and precedence are explained by [the edition guide](docs/RELEASE_READINESS.md); the adopted instructions and hashes are recorded in [PUBLISHER_APPROVAL.json](PUBLISHER_APPROVAL.json).

Additional catalogue samples, generated references, a Japanese manual and integrity/coverage tooling were prepared for this distribution. Original samples 01–25 remain unchanged. Production examples 01/02 were migrated explicitly from the historical companion 0.1.0 to the current 0.2.0, without inventing plugin functionality.

## Synthetic assets

`examples/production/assets/example-audio.wav` is the source package's synthesized 440 Hz test tone. `example-plugin-state.bin` is the source package's deliberately invalid 47-byte illustration, not a working plugin state. `mono-silence.wav` was generated for this package as 11,025 zero-valued PCM16 mono samples at 44,100 Hz (0.25 seconds). No commercial recordings or voicebanks were added.

All example plugin names/IDs are fictional, descriptive data. Neither a format identifier nor a device-state URI grants permission to instantiate software. Core Resource descriptors may name external bytes that are not in this distribution; they must not be confused with bundled Production assets.

No DAW, independent parser, plugin, DSP host, singing application, WAN service or robot hardware was used to establish compatibility. Static parsing, schema content comparison, selected reference checks and file hashing during assembly are not such evidence.

Upstream license notices and the CC0/MIT texts are retained. This notice does not independently authenticate authorship or rights to every contributed byte.
