# Source reconciliation — OSTF 4.3.0

## Immediate source

The source is the publisher-approved conversation artifact `OSTF_4.3.0_Publisher_Approved_Specification.zip`, SHA-256 `1440d16a440ba26d679bf940fe4fc8a68c5ad86c9944c6e35471bbbc7fdd6351`. Its nine normative files were compared with `OSTF_4.3.0_Publisher_Approval_Record.json` and retained unchanged. See [edition guide](RELEASE_READINESS.md) for the complete per-file fingerprints.

## Inherited 4.2 baseline

The included `schema/ostf-4.2.0.schema.json` has SHA-256 `6933e2b52332e8b58b9c34b53ca7e101c3f0b689fd5f50f593809480b35e0fa2`. The source release records this as the published 4.2 baseline from `https://github.com/yoh-nak/Open-Song-Timeline-Format-4.2`. The source release also records the inherited complete manual digest `9ee80e7d401f0cb5330d755c190ebd1afc4cfdb80c8b0785bd6de6c36c01cdf5` and the 4.2 parameter-reference digest `d1673ceb3adfc7cbe61d1fce02b78983731fe3315a7d4628ee0a3e96dcc91bb7`.

These are source-package provenance records, not a claim that this packaging operation independently re-fetched or legally audited the upstream repository. The new parameter references are generated directly from the supplied frozen active schemas. The English implementation manual retains the complete inherited musical material while updating distribution-specific links and instructions.

## Changes for distribution

The adopted normative corpus and Core examples 01–25 are unchanged. Newly authored catalogues and descriptive wrappers add no Core fields. Production examples 01/02 were explicitly re-enveloped as 0.2.0. The new mono-silence asset is generated from zero-valued PCM16 samples. The package record documents these distinctions without inventing contributor signatures or external test results.
