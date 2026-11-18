# Facts, events, and measurements

Consolidate facts from different materials for comparison without rereading every document.

Navigation: [INDEX.md](INDEX.md), [topics](topics/AGENTS.md). Contract: [thematic consolidation](../documentation/specs/consolidate-records.md).

- [DATABASE.md](DATABASE.md) defines optional derived-database rules. The agent determines schema, sources, and builder from actual data and tasks.
- Before answering from a database, check integrity, input hashes, and coverage. New or changed sources require a verified rebuild; never present an old representation as automatically updated.
- Each fact links to a material and an accessible location in its source.
- Distinguish measurements, user reports, diagnoses stated in reports, and clinicians' prescriptions.
- Preserve original values, units, reference ranges, and dates; identify transformations separately.
- A prescription does not confirm actual medication use. Missing information does not mean no event occurred.
- Preserve contradictory records with their sources; never silently replace them with one value.
- Consolidate confirmed duplicates into one event. For discrepancies, show status, a working value with rationale, or an open question. Preserve original variants for traceability.
- Hypotheses and recommendations are not facts in this layer.
- A fact absent from a derived database is not necessarily absent from the project. Always state database coverage explicitly.
- [measurements](measurements/AGENTS.md) — ongoing observations organized by measurement date; [contract](../documentation/specs/measurements.md).
- [medications](medications/AGENTS.md) — ongoing actual-intake tracking from user reports; [contract](../documentation/specs/medication-tracking.md).
- The primary lab document takes precedence for lab results. Use a workbook summary when the corresponding primary result is unavailable, explicitly recording provenance. Match the actual test, not just its date and a similar name; preserve conflicts. Basis: [architecture](../documentation/ARCHITECTURE.md).
- Ask how entries were made in each workbook; do not transfer provenance assumptions from other workbooks. Without a primary document they may serve as user-provided information. Mark individual typos locally rather than excluding the whole workbook.
