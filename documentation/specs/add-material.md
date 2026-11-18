# Adding a material

This contract applies to files, related file sets, and user messages. Determine extraction methods and verification coverage for each source. Automatic OCR requires a separate tool and verification. Requirements: R-001 and R-002 in [REQUIREMENTS.md](../REQUIREMENTS.md).

## Input
A file, related file set, or user text, with available provenance and event-date information. A chat request may be the entry point; no automation mechanism has been selected yet.

"Import this document" is enough to trigger the complete contract. The user need not separately request original preservation, full-text recognition, field verification, duplicate detection, or uncertainty reporting. The agent performs all these steps. If information is insufficient for correct intake, ask a specific clarification while preserving the source and established facts.

## Result
- Originals in raw, linked by a stable material identifier.
- A card and complete readable text in materials. The card contains type, provenance, event/receipt dates, summary, original links, and verification status.
- Text linked to pages or accessible original locations, with explicit illegibility markers.
- Structured content under the [material format](material-format.md): lab results have explicit columns for values, units, reference ranges, and source flags. Date directories mirror originals.
- Where needed, facts in records and an updated overview with evidence links. Fact extraction is not a prerequisite for preserving an original.

For a multiyear archive snapshot, the export date from its contents determines its directory, not an individual measurement date. Record the event range separately. See [archives and exports](archive-import.md).

## Processing and verification
1. Check the index and checksum for prior intake; a resubmission is not automatically a new medical event. The inbox is incoming/; originals stay there until intake is completed.
2. Record the original checksum. Extract existing text or use OCR; for nontext data preserve an available description and limitations.
3. Compare dates, numbers, units, reference ranges, medication names/doses, and important report wording with the original. Mark unverified information explicitly. After reading, determine [type and content domains](material-classification.md) and record classification and rationale in the card and manifest. Classification is not health analysis.
4. Prepare the card and check the path from a specific value or statement to its original.
5. Check readiness of the card, full text, page references, and future original path. Only after successful verification move the original to raw/YYYY-MM-DD/ by medical event date (sample collection for lab results). Unknown dates or failed checks defer the move. Never overwrite existing files.
6. After moving, verify unchanged checksums and accessible links. Only then mark intake complete. Report what was added, what was checked, and what still needs clarification.

After updating the manifest, run `python -B scripts/materials.py verify` from the project root yourself. It must succeed before intake can be completed. It complements, not replaces, comparison of contents against the original.

### Exact resubmission
If checksums differ but a scan represents an already accepted document, compare patient, request number if available, dates, all results, units, reference ranges, flags, and important text. If equivalent, add it as additional_representations under the [material format](material-format.md), without duplicate measurements. Explicitly record differences and cropped regions; matching names and dates alone is insufficient.

A received document fragment can be accepted with explicit incompleteness. Do not hide missing pages or illegibility behind completed-intake status. An unknown date still defers moving; preserve user confirmation as a separate date rationale. Temporary scripts and images may be in temp/, but cards, manifest, and archive must not depend on them.

Use shared [scripts](../../scripts/AGENTS.md) for recurring technical operations. intake.py prepare verifies the prospective manifest, cards, and index links before writing cards. accept repeats verification before moving originals, then archives without overwriting and publishes the manifest and index. In related_materials, put the identifier in id. The agent verifies contents against the original.

Save the receipt before cards; it contains their prepared text and hashes. If a failure occurs after the receipt is saved, run accept with it. The command restores missing cards, replaces the manifest, and updates statuses without adding records twice. Status changes preserve source text verbatim. Keep the receipt in local temp/ until verify succeeds. Unregistered originals/cards and incomplete statuses block verify. Concurrent publication of multiple batches is unsupported: a manifest changed by another operation stops recovery for review.

If a lab's collection date is unknown, use its issue date as the directory only on explicit user instruction: event_date: null plus separate document_date, catalog_date, and catalog_date_basis. Never present the directory date as collection date. For a composite scan, keep component dates separately and choose the directory by an explicitly identified primary document; a shared topic does not make one event. Describe a form repeated in several scans as shared content linked to all views, without duplicate measurements.

Use YYYY-MM-DD in intake configuration. A laboratory card with a known collection date uses that directory. In an additional representation, date names the existing card directory, even if event date is unknown. One original can serve multiple cards with nonoverlapping regions. If a batch contains identical bytes under different names, handle resubmission first. Differences in lab-row signs, units, ranges, and flags require verification. A simple decimal comma and point are equivalent numeric notation when other fields agree.

If full SHA-256 matches an accepted original, check that the canonical material is accessible. Do not create another card, measurement, or medical event. Record the submission in duplicate_receipts and link it to the existing card. After checking, preserve the duplicate copy in the same date directory under a separate name without overwriting, and verify SHA-256. Do not silently delete it. Matching filename, date, or request number without matching contents does not establish duplication.

For multifile documents, check every originals checksum and the set-checksum scope under the [material format](material-format.md). A matching page does not prove the entire document was resubmitted. On direct user instruction and confirmed content continuity, accept pages as one card with order and separate source locators.

## Uncertainty
Personal reference information without an established compilation date may complete intake in mirrored raw/undated and materials/undated: reference_information, event_date: null, document_date: null, separate directory rationale, and the user's verbatim time indication. Do not substitute receipt date, January 1 of an assumed year, or a similar test's date. Such a collection creates neither a medical event, clinician prescription, nor completed examination. This does not waive deferral of medical lab results with unknown dates. Basis: [architecture](../ARCHITECTURE.md).

On recognition error, the original remains available and the material is marked incompletely processed. Do not guess missing values. Current identifiers and fields are in material-format.md; universal versioning remains an open question.

## Practical contract verification
Add a real material, locate a fact through its card and text, then compare it with the original. Record losses and usability problems before adopting format decisions.
