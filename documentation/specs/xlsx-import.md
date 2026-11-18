# Personal health workbook intake: XLSX

Read a multi-sheet workbook without changing XLSX. Establish sheet roles, units, and input provenance separately for each workbook.

## Input and result
Keep unchanged XLSX in raw; one snapshot card in the mirrored materials directory and a complete data directory alongside it. Snapshot date does not replace event dates. Use the filename and available metadata as snapshot-date evidence; record conflicts.

The readable result provides navigation to every sheet and its role, all nonempty cells with addresses, original types, formats, formulas, cached values, and raw OOXML values. The original retains formatting, charts, and objects; empty cells do not establish absence of graphics.

## Roles and uncertainty
- Distinguish direct user measurements from secondary laboratory summaries, calculated values, and medication history. Do not assume instruments or precision without source information.
- Ask the owner how entries in each new workbook were made; do not automatically assume manual entry. Without a primary document, workbook results may be used as user-provided information; mark errors individually. Manual entry does not automatically disqualify data.
- Empty calendar rows are not measurements; empty values are not zero. For multiple date blocks, keep each measurement linked to its local date.
- For repeated lab results, preserve primary-material links and verification limits. A summary snapshot does not automatically create duplicate medical events. Do not substitute consultation/printing dates for collection dates.
- Prefer the corresponding primary document for a lab result. Use the workbook when a result is absent from available primary materials, marking it as secondary. Match patient, test, date/sample, units, and method where available; do not merge uncertain cases. On conflict, the document determines the working value while the discrepancy and summary entry are preserved. An erroneous date type or unverified workbook number does not become reliable because no document is available.
- Direct regular measurements may extend ongoing [measurement series](measurements.md). Snapshot date remains provenance, not observation date; subsequent entries continue in records without requiring a new workbook.
- Preserve a result stored as an Excel date with its original type, number, and format. Guessing a value from day/month is not a correction.
- Distinguish zero from below-detection-limit values. Flag unusual units/ranges and unmatched dates; do not silently normalize them.
- Preserve formulas literally. A verified limited expression set may be evaluated separately for readability, labeling derived provenance. Leave unsupported formulas unevaluated. This is not recalculating XLSX in Excel.
- Medications listed in a user spreadsheet do not confirm current therapy or compliance with a prescription.

## Verification and tools
The shared [xlsx_extract.py](../../scripts/xlsx_extract.py) extracts without writing to XLSX. Before moving, verify sheet/cell completeness against XML, original integrity, control examples of formulas/dates, and address locators. State exact primary-form cross-check coverage; do not call a sample a complete verification.

Register derivatives in derived_files with SHA-256; materials.py verify checks their availability and hashes. Distinguish successful intake from reliability of user content. Follow the general [contract](add-material.md) for moving and cleanup.
