# Original materials

Original lab results, reports, prescriptions, images, measurement exports, and user notes are stored here.

- Preserve received contents unchanged. Put recognized text and corrections in `../materials/`.
- A material may comprise several files. Describe their relationship in its card.
- Distinguish receipt dates from medical event dates; do not guess unknown dates.
- Read the [intake specification](../documentation/specs/add-material.md) before processing.
- [incoming](../incoming/AGENTS.md) is the explicit inbox for unprocessed files. The raw root is not an inbox. Place completed materials in `YYYY-MM-DD` directories by medical event date only after successful intake verification. Leave originals in incoming on failure.
- For lab results, use the sample collection date, not the print date or project registration date. If it is unknown, do not guess; defer the move.
- [undated](undated/AGENTS.md) holds completed undated reference information, including personal collections; an unknown compilation date does not block their intake. These are not dated medical events. Basis: [architecture](../documentation/ARCHITECTURE.md).
- For a multiyear export snapshot, use the explicit export date from its contents and record event coverage separately. See [archives and exports](../documentation/specs/archive-import.md).
- Moving must neither alter original contents nor overwrite an existing file. Verify checksums and links afterward.
- Basis: [intake rules](../documentation/specs/add-material.md).
