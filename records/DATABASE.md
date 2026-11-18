# Derived database for queries

A database is optional. Use one in records when scale and tasks require joint queries across many facts. Originals, readable materials, and records with provenance remain the evidence; the database is a reproducible representation.

## Choosing a structure
The agent chooses schema, format, and sources from actual data and the user's task. SQLite may suit recurring queries, for example. The template contains no ready-made database, mandatory source list, or application-specific builder. Do not create empty fields for absent services, fixed layouts from someone else's workbook, predetermined measurement tables, or provider priorities.

## Build requirements
- Explicitly state coverage: sources, period, included and excluded information types.
- Preserve stable fact IDs, all representations, variants, open conflicts, and selection rationale. Duplicates do not increase event counts.
- Link each value to its material, exact locator, and original. Register all inputs affecting calculations with checksums, including linked files.
- Establish units, timezones, calculation methods, and field semantics from sources; do not infer them from numbers, app names, or column positions.
- Determine reconciliation and selection rules from contents, without a permanent priority based on service name. Do not hide unresolved cases in summaries.
- Distinguish observations and calculated aggregates. NULL is not zero; an observed-day average is not a calendar-day average.
- Do not edit the database and source records as independent versions of one fact.

## Application-specific scripts
Create the necessary builder and queries after studying accepted materials. Test the first version in temp. Save reusable scripts in scripts with inputs, schema, dependencies, verification, and limitations. Configuration references only actual sources within the project; do not embed medical data in code. Verify the builder before using its results.

## Verification and use
Build into a new file. Check integrity, relationships, source-record coverage, input hashes, deduplication, and preservation of manual resolutions. Every source record links to a fact or an explicit exclusion reason. Do not answer from a partially built database.

Check input freshness and coverage before querying. Open SQLite read-only. A new source or changes to data, schema, or selection rules require a verified rebuild, not assumed automatic updates. Show coverage and missing data alongside averages and totals.

Joining observations by date does not establish causality. Old outputs remain dated snapshots and do not update automatically.
