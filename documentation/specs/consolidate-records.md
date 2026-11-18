# Consolidating materials into shared facts

Contract for reconciling facts across sources. Choose topic/fact formats according to content while preserving stable identifiers, evidence, and correction history.

## Purpose
materials holds a processed representation of each source. records consolidates a shared history: facts/events, ongoing measurements, topics, duplicates, and discrepancies. A topic reader sees currently selected facts and open questions without rereading every card.

This is a separate operation after intake. Grouping cards in the material index helps locate sources but does not reconcile their facts.

## Result
- Topic views in records/topics/, such as endocrinology or cardiology, using material domain codes.
- Facts with stable IDs, type, medical date, value/unit, and precise evidence. One fact may appear in several topics without independent copies.
- Ongoing series in records/measurements/; topics link to a series instead of duplicating the full table.
- For each significant discrepancy: variants, sources, status, selected value if any, selection rationale, and remaining question. Decisions about individual medical facts belong here, not in the architectural decision log.

## Reconciliation
1. Determine whether records describe one event: patient, measurement/test, date and sample/request, method, units where available. Different collections, conditions, or times are not contradictions merely because values differ.
2. Link confirmed duplicates to one event. Reprints, scans, and summary entries do not create new measurements.
3. Distinguish reading/input errors, unit differences, different events, report versions, and genuine unresolved discrepancies. Do not infer missing data by guesswork.
4. Prefer the primary lab document. If unavailable, use the workbook entry as user-reported data. If the owner confirmed manual provenance, absence of a primary form alone does not prohibit using the entry.
5. Flag specifically suspicious cells individually. An Excel date instead of a result is not a usable lab number. Isolated typos do not disqualify the entire workbook.
6. With sufficient evidence, publish the working value and explanation. Otherwise keep the question open and show variants; never select by majority of copies. Preserve sources and earlier variants.
7. A new primary document may confirm or replace an earlier user fact's evidence while retaining event links and correction history.

A document's priority for a lab number does not automatically resolve conflicting diagnoses or treatment choices. Prescription, actual-intake report, and calculated dose are different information types. Medical interpretation remains in overview/outputs.

## Practical verification
### Events from multiple sources
Readable materials remain independent sources. The shared history uses reconciled events, not the sum of export rows. An event may have several representations with different IDs, precision, and measurement sets.

- Preserve each source record and exact locator. Link confirmed representations to one stable event ID.
- An exact external ID may establish a link. Without one, verify combined substantive features, dates, known timezones, and conditions. One day or a similar value is insufficient. Base tolerances on verified source precision.
- Keep ambiguous matches as candidates. Show their coverage effects explicitly; neither hidden double counting nor silent exclusion is allowed.
- Reconcile measurements separately from event identity. Different duration definitions and original/calculated quantities are not interchangeable. Preserve variants and selection rationale; do not prioritize by service name.
- Every source record links to a fact or an explicit exclusion reason. Count a confirmed event once. Create handlers after studying actual formats and verifying rules on user data.

Use a [derived database](../../records/DATABASE.md) if needed. Topic Markdown and machine-readable facts must not become independently editable copies of one history.
