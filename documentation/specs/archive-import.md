# Archive and export intake

Extends [material intake](add-material.md). Applies to document archives, app/device exports, tables, and observation streams. Determine structure from actual contents, not a preselected service.

## Inputs and dates
Accept one export as a snapshot material with an unchanged original. Its export date determines the directory; retain individual event dates internally. Ask the user if an explicit export date is missing. ZIP-member timestamps or query boundaries do not by themselves establish export date. Store event coverage separately.

## Preparing a handler
Inspect the particular source's contents, format, schema, units, locators, and field semantics. If a shared tool is insufficient, create an application-specific script in task context. One-off processing belongs in temp; verified reusable operations go in scripts with commands, dependencies, and applicability limits. Do not create mandatory fields, filenames, column positions, or settings for sources absent from the user's data. Never embed personal information in code.

## Complete representation
- Preserve the archive and check SHA-256. For ZIP, check CRC, member inventory, duplicate names, and path safety. Do not execute contents or load external XML schemas/styles. Keep processing within acceptable resource limits.
- CSV preserves original headers, column positions, string values, empty cells, and record numbers. Do not merge identically named columns.
- XML/JSON preserves attributes, text, nested structures, order, and repetitions with element locators. Never silently discard unknown fields or types.
- Preserve complete time series and routes. Do not reduce points or round coordinates without identifying a derived representation separately.
- Preserve PDFs/images with page-linked text and explicit visual-verification coverage. Parallel printed and tabular versions are not automatically independent events.
- Do not duplicate service access keys in readable copies. Explicitly list concealed fields; retain the complete original and respect its confidentiality.
- Link the card to the complete data directory, inventory, tables, and checks. Register permanent derivatives in derived_files with checksums.

## Meaning and reconciliation
Preserve original numeric strings, units, dates, timezones, and repetitions. Do not guess unlabeled units or category meanings from similar names. User input, device measurements, targets, and source calculations differ. Closed intervals and unfinished timers are not interchangeable. Missing records do not become zero; time in bed does not become sleep duration.

An exact external ID or verified substantive match may link representations of one event. Preserve all evidence and variants; do not merge events based only on one day or a similar number. Do not prioritize a service by name. Leave ambiguous links unresolved and state their effect on calculation coverage. Consolidation into records is separate under its [contract](consolidate-records.md).

## Verification
Compare source records again with the complete derivative, including element count/order, nesting, all cells, locators, ranges, and repetitions. Check copied archive members byte-for-byte; check transformations under a documented rule with independent completeness verification. Sampling does not establish completeness. Check unchanged originals, derivative registration, and link navigation before finalizing intake. Preserve unsupported sections and verification limits in the card.
