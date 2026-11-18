# Shared scripts

Inherit the root rules. This directory contains repeatable operations shared across different sources. Do not hard-code the user's medical data.

## Source-specific processing

The agent creates a source-specific processor after examining the actual document, archive, or export. Do not assume a particular service, manufacturer, filename, export schema, column, or unit. Specific data providers may appear in documentation only as explicitly labeled examples.

Put one-off scripts and intermediate results in temp. Save verified, repeatable operations here, documenting commands, inputs, outputs, dependencies, and applicability limits. The user does not manually define the source format or domain rules: the agent investigates the data and asks only about missing meaning.

Before using a new processor, check that the original is unchanged and verify extraction completeness, numbers, units, dates, locators, duplicates, and ambiguities. If verification is impossible, do not declare the result reliable or intake complete.

## Shared operations

- [materials.py](materials.py) — `verify` checks the registry, classification, SHA-256, links, regions, and index; `index` rebuilds navigation from the registry. Standard library.
- [intake.py](intake.py) — `prepare temp/reviewed.json temp/receipt.json` and `accept temp/receipt.json`: prepare previously reviewed material, check inputs and links, archive without overwriting, and update the registry and index. The input format is documented in the script. The agent performs OCR and content review. The receipt is written before cards. Keep it until verify succeeds so interrupted intake can resume. Resume publication with the same accept command: the registry, cards, and index are each replaced atomically; retries do not add duplicate entries.
- [image_views.py](image_views.py) — `preview INPUT_DIR OUTPUT_DIR --prefix PREFIX`, `orient CONFIG_JSON`, `inspect INPUT OUTPUT.png`: thumbnails, copies with documented rotation, and temporary readability enhancement. For `orient`, `archived_source` must point to an existing original in `raw/` with the same SHA-256. Requires Pillow. Originals remain unchanged; improved contrast does not prove that characters were recognized correctly.
- [xlsx_extract.py](xlsx_extract.py) — `INPUT.xlsx OUTPUT_DIR`: extract cells, types, formulas, cached values, and OOXML without changing the workbook. Requires openpyxl 3.1 or later. The agent determines sheet layouts, units, and semantic relationships for each new workbook.
- [medications.py](medications.py) — `verify`, `status --as-of YYYY-MM-DD`, `render --as-of YYYY-MM-DD`, `add-event COURSE_ID EVENT_JSON`: track user reports under the [contract](../documentation/specs/medication-tracking.md). Expected intake does not become confirmed as time passes. State is calculated by effective_date, then recorded_date, then message order for equal dates. A visible correction replaces a checkpoint at its original position. When the last intake date is unknown, a checkpoint stores `last_intake_date: null` and the cumulative quantity. Calendar projections require a known last intake date. `status` includes REPORT messages as separate rows. `--courses-only` retains course states only.
- [plot_history.py](plot_history.py) — `INPUT.json OUTPUT.png [START_DATE]`: chart verified series. Requires Pillow. The input schema is in the script; the agent specifies sources, limitations, and value selection. HEALTH_FONT lets you supply a TTF font for the chart labels.
- [check_project.py](check_project.py) — check structure, local links, anchors, JSON, and Python syntax. `--empty` checks the initial empty state. `--privacy` enables heuristic scanning for suspicious strings before publication. Read-only.
- [smoke_test.py](smoke_test.py) — isolated checks of intake, preservation, recovery, change detection, and tracking based on fictional reports. On success, only the directory created by the test is removed. Includes late reports and registry, card, and index write failures.

## Intake and placement

Read the destination directories' rules before running commands. The representation's output directory must have AGENTS.md. The intake date field selects the directory. An unknown event date stays null and requires a separate catalog_date_basis; do not present the document date as the sample collection date. Undated reference information may use reference_information and the undated directory under the [contract](../documentation/specs/add-material.md).

One document may have several originals; a shared scan may have non-overlapping source_regions. Box coordinates are normalized against the original image before rotation. archive_date separates the shared carrier's directory from the card date. See the [material format](../documentation/specs/material-format.md).

Register all permanent derived files in derived_files with path and sha256. Cards and final data must not depend on temp. The agent handles exact resubmissions under the contract: intake has no ready-made command for duplicate_receipts.

## Dependencies and checks

Python 3.11+. Core intake and checks use the standard library. Optional packages for shared operations are listed in [requirements.txt](../requirements.txt). The agent selects and documents dependencies for source-specific processors.

Do not run checks with -O: some scripts use assert. File checks do not replace medical content review. Commands: [CHECKS.md](../documentation/CHECKS.md).
