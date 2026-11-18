# Project checks

## Structure and links
From the project root:
```console
python -B scripts/check_project.py
```
Checks required files and primary-layer AGENTS.md, local Markdown links/anchors, Python syntax, JSON, and JSONL. It changes nothing. Add `--empty` to check a new empty copy. That mode checks the complete file list and checksums of working layers, including initial instructions, indexes, and medication summary. For intentional starter-content changes, verify them first, then update the baseline hashes in the [checker](../scripts/check_project.py). Check populated projects without --empty.

Before publishing a clean template, run `python -B scripts/check_project.py --empty --privacy`. --privacy heuristically searches for paths, contacts, keys, and .env files outside excluded temporary directories and environments. Review findings under [privacy rules](PRIVACY.md).

## Materials and sources
```console
python -B scripts/materials.py verify
```
Checks manifest, classification, original and registered-derived SHA-256, source regions, and consistency of card identifiers and links with the manifest. Also checks the index and detects unregistered cards and originals. Regenerate the index separately:
```console
python -B scripts/materials.py index
```
File verification does not confirm medical accuracy. Check important numbers, units, dates, and prescriptions against original pages under the intake contract.

## Medication intake
```console
python -B scripts/medications.py verify
```
Checks course definitions, material links, and message validity. Taken counts change only with user reports. Read state with status and an explicit `--as-of YYYY-MM-DD`.

## Isolated operation checks
```console
python -B scripts/smoke_test.py
```
A separate temp directory tests fictional-source intake, overwrite protection, modified-source detection, interrupted-copy recovery, and intake tracking. Working data is unchanged. Tests include late reports, corrections, and resuming intake after manifest, card, and index write failures. verify must detect incomplete publication; repeating accept must not duplicate entries.

Add `--formats` to check XLSX extraction and image rotation. This requires [requirements.txt](../requirements.txt) dependencies. Details: [examples](../examples/README.md).

Do not use -O: some scripts rely on assert. On failure the test directory remains for inspection; after success only that directory is removed.

## Extending processing
For a new format, verify extraction completeness, unchanged originals, preservation of units, dates, locators, and uncertainties. First test a small understandable source. Keep material-specific limitations in the card and changed capabilities in CURRENT.md. Programmatic checks alone cannot establish medical validity.
