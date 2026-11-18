# Readable material format

Purpose: quickly understand one document and reduce reading and later fact-extraction errors. This is a document representation, not medical analysis.

## Placement
materials/YYYY-MM-DD/MAT-<identifier>.md corresponds to an original in raw/YYYY-MM-DD/. Intake rules determine dates and links. Shared INDEX.md and manifest.json are at the materials root. For new document types, determine material boundaries from contents; do not automatically split a multipage document.

When several files represent one document, create one card with page order, grouping rationale, links, and each original's checksum. Use originals entries with order, path, and sha256 in the manifest. With sha256_scope: ordered_original_sha256_bytes, material sha256 is the set digest: SHA-256 of the concatenated binary 32-byte file digests in order. Without that scope, a single-file material still uses its original file's checksum. Verify all originals, not the set digest against a single file.

A large archive card links to an adjacent MAT-<identifier>-data directory containing readable tables, schema, full streams, and a verification report. The export date from contents determines the snapshot directory; event coverage is separate. Preserved structured fields avoid copying megabytes of XML into Markdown; original text remains in the archive. See [archives and exports](archive-import.md).

A lab PDF may have an adjacent MAT-<identifier>-laboratory.json with full selected-page text, metadata for each printout, all row occurrences, and analytes groups. laboratory_data and laboratory_data_sha256 connect it to the card in the manifest. Preserve alternative units, ranges, and flags within groups with physical page numbers; identical reprint occurrences do not become new measurements. event_key joins request identifier, collection date, and normalized name within the material: this is technical source grouping, not a global medical-fact schema.

A PDF containing independent forms can support several cards: pdf_pages identifies physical pages, and scope_analytes in lab data specifies analytes within a shared summary printout. The checksum remains that of the entire PDF. Add forms matching existing scans to their cards' additional_representations; new forms in the same container get new cards. Structured row scopes must not overlap. A matching date and request identifier without content verification is insufficient.

For repeat cross-checks preserve row-level evidence in MAT-<identifier>-cross-check.json; on a substantial addition preserve the old scan text in MAT-<identifier>-scan-v2.md, linked from the new card. Once a complete PDF is available, do not keep old incompleteness limitations as current; distinguish the old scan's limits from the available versions' completeness. Do not change identifiers or old-original checksums.

### Independent documents in shared scans
A scan may contain unrelated documents, and two sides of one document may be in separate scans. A card represents a medical document, not necessarily a whole file. Use source_regions for verified regions: original path and top, bottom, or whole in original orientation. Document viewing rotation separately. Regions belonging to different cards must not overlap; whole overlaps either half. Top/bottom specify document membership, not precise crop coordinates.

Such cards have a stable region suffix after MAT-<hash>. SHA-256 remains the digest of the full original or set, not the cropped fragment. Archive the complete original once. In intake.py, scope_key and source_regions define membership; archive_date can separate an agreed shared-carrier date from the card directory date. source_archive_date preserves this in the manifest. Each card keeps its own document/event date; adjacency in a scan implies no medical relationship.

For a record card spanning several dates, retain every entry's date and the unknown compilation date separately. An agreed directory date does not replace event dates. medical_record distinguishes a record card from a clinical consultation.

## Reading order
For more than two documents or side-by-side placement, source_regions permits region: box and bounds: [x0,y0,x1,y1]: normalized 0–1 coordinates from the top-left of the **original image before rotation**. Rectangles must have positive area and be inside the image. Shared edges are allowed; area intersections are rejected, including with top, bottom, and whole. This is navigation within a full scan, not physical cropping. For different carriers of one document, files[].archive_date separately defines each complete scan's directory by its primary document; component dates stay in the card. Basis: [architecture](../ARCHITECTURE.md).

Store an additional scan of an accepted document in its existing entry's additional_representations: path, sha256, kind, registered_date, status, equivalence_basis. Keep the canonical original, identifier, and digest scope unchanged. State equivalence rationale and scan limitations in the card. This is not an exact byte duplicate; verify content identity separately.

Distinguish source completeness and transcription quality from completion of received-file intake. For explicitly missing pages use document_completeness with status: partial, expected_pages, received_pages, and missing_pages. For obscured text use status: partially_obscured and obscured_fields. Mark partly readable handwriting transcription_completeness: partial with unresolved_fields. Completed intake implies neither full transcription nor a complete source; display limitations explicitly.

1. Title and short card: patient, type/subtype, primary/additional domains, event date, document date, source, ID, and verification status. [Classification rules](material-classification.md).
2. Contents: sections and number of measurements. For labs, list laboratory flags without your own diagnosis. No flags does not mean normal results.
3. Complete structured contents: lab tables; report sections for complaints, history, findings, conclusions, and prescriptions with authorship preserved; other materials in an appropriate representation.
4. Source comments and a separate uncertainty block: unspecified, unverified, ambiguous, or contradictory information.
5. Technical details and complete page-by-page extracted text for verification.

## Laboratory results table
One row per analyte. Columns: name, result, unit, source reference range, laboratory flag, source page.

- Preserve numerical precision and signs <, >, ≤, ≥. Never silently round, supply units, or convert values.
- Laboratory flags come only from the source. Represent an absent asterisk as "none", not "normal". Your own comparison with a range is not a laboratory flag.
- Mark absent units or other fields "not specified"; absence is not zero.
- Join wrapped names without losing content; document whitespace and line-break changes. Do not merge relative and absolute values even when names look similar.
- Keep analyte and equipment comments explicitly linked to their rows.
- If a flag conflicts with printed values, do not correct the source; describe the discrepancy separately.

## Verification
For graphical examinations preserve images and fragment navigation, using copies with documented rotation if necessary. Text does not replace plots. Distinguish instrument numbers, clinician conclusions, and independent measurements; do not reconstruct an illegible conclusion from curve shapes.

Check every row against the original: name, result, unit, range, flag. Check row count, wrapped names, source page, and shared dates. Preserve complete text as an additional checking aid, not a table substitute. Graphical details remain in the PDF.

Changing a representation does not alter the PDF or material identifier. Record representation version and verified coverage in the card and manifest. One batch does not establish suitability for all document types.
