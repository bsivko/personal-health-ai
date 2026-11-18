# Fictional demonstration

All values, dates, names, and messages below were invented to test the mechanics. They are neither a real person's medical data nor treatment recommendations. Demo files are not registered in the working materials/records layers.

## Safe execution

From the template root:

```console
python -B scripts/smoke_test.py
```

The script creates a separate copy of the scaffold in `temp/`, populates only that copy with fictional sources, and checks prepare/accept, checksums, overwrite prevention, detection of corrupted sources, and medication tracking behavior. The owner's working data layers are neither copied into the test directory nor modified. On success the test directory is removed; on failure its path remains in the message for investigation. The test reads AGENTS rules.

Do not run fictional intake directly in your working history. For manual exploration, create another separate copy of the empty template.

## Input and intake in a separate learning copy

`demo-lab.txt` and `demo-product.txt` are explicitly fictional plain-text originals. `reviewed-intake.json` contains a previously checked representation, the full table, document details, classification, and the exact SHA-256 hashes of those files. This is a learning example; for a real document, prepare the content and hashes after reading the source itself.

In a separate copy, the agent reads the root and local AGENTS files, then:

1. Copies these two files into incoming without changing their bytes.
2. Creates raw/2000-04-02 and materials/2000-04-02. In each, creates and reads AGENTS.md inheriting `../AGENTS.md`; cards and originals have matching directory dates.
3. Copies reviewed-intake.json to temp/reviewed.json and runs:

```console
python -B scripts/intake.py prepare temp/reviewed.json temp/receipt.json
python -B scripts/intake.py accept temp/receipt.json
python -B scripts/materials.py verify
```

`reviewed: true` is allowed only after actual review. Until accept, originals remain in incoming and cards have a pending status. After success, verify SHA-256, the registry, and the index; the receipt and your intermediate files can then be removed.

A failure between copying and deleting the source can be recovered with the same receipt if both copies have the expected hash. A partially written or modified archive file stops the operation; the source is not deleted. Do not rerun prepare over existing cards. Preserve the receipt and check both copies before a manual repair. A registry, card, or index write failure can also be recovered by rerunning accept with the same receipt. A registry changed by another operation stops the retry. Each file is published atomically, but updating multiple files is not a single transaction: the result remains incomplete until verify succeeds.

## Examples of subsequent layers

`measurement.json` is one fictional user observation. After its format is checked, an entry like this belongs in a series' JSONL file for the observation year, not in the import folder.

`course.json` and `course-events.jsonl` contain a sample regimen and one report of a quantity taken of the fictional DEMO product. Its material_id is derived from demo-product.txt. The fields and links refer only to the isolated learning copy after intake; this is neither the owner's active course nor an instruction to take medication. The test shows that moving to a future date does not increase the quantity or automatically complete the course. A planned course does not become active just because time passes either.

`plot.json` contains fictional points with explicit provenance. In a separate copy with Pillow:

```console
python -B scripts/plot_history.py examples/plot.json temp/demo.png
```

If a suitable font is unavailable, set `HEALTH_FONT` to the path of your TTF font. The image is not overwritten. Shared plotting tools do not extract data or reconcile medical facts themselves; the agent prepares and verifies the input JSON.
