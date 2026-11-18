# Ongoing measurements

Contract for ongoing observations from messages, documents, and devices. Verify format, units, provenance, and corrections separately for each new measurement type.

An ordinary measurement message triggers the procedure. Preserve it as the source with original value/unit, date precision, and unknown unreported fields. The user need not request preservation of their message or prohibit guessing. Resolve relative dates such as "today" from the message date in a known timezone while retaining the original wording. Ask for missing required information, not optional time, conditions, or method.

Before completing entry, reread the saved observation and check value, unit, date, and quotation against the message; verify ID, provenance, and possible duplication. Link corrections to prior records. Verification is mandatory without a separate request.

## Ongoing series
Keep weight, body circumferences, sleep, and activity in records/measurements/ by measurement type and observation date. Continue the series as records arrive; a workbook import adds historical observations with provenance. Upload date determines neither medical date nor series name.

Keep the workbook as an unchanged original source in raw and materials. The working series does not live inside its import directory. New measurements can arrive in chat or files; no new workbook is required. Store user message text/available identifier, receipt date, and stated measurement date directly in record provenance.

## Observation contents
- Stable identifier, measurement type, original value and unit.
- Measurement date; time and timezone only when known. Never invent midnight for date-only observations.
- Conditions and method if reported, such as morning, fasting, or home scales. Explicitly preserve missing information.
- Source: material and precise sheet/cell locator, user message, or device source. Distinguish derived from directly recorded values.
- Separate registration and correction times. IDs must not change when a source is added or a file moved.

Several measurements in one day are valid. Matching date and measurement type does not establish duplication; conditions/times may differ. Reimporting the same source cell does not create a new observation. Add evidence to the existing observation for a confirmed same event. Preserve corrections with the previous value and rationale; never silently overwrite history.

## Workbook history
Transfer only populated measurements with their date block's local date. Empty calendar rows are not observations. Date formulas may supply dates, not create measurements. Store exercise totals or measurement ratios as derived values with original formulas.

Units absent from the workbook require confirmation; do not infer them from magnitude. Do not label two columns under "Sleep" as actual/planned without evidence. Do not automatically combine examination weight and home weighing.

Boundary check: cells from different date blocks use their own block's local date; snapshot date stays a source attribute.

## Provisional physical storage
The working format for first-transfer verification is records/measurements/<measurement>/<year>.jsonl, one observation per line. Keep a short measurement/unit catalog alongside; generate readable tables and charts from series. Do not use an import directory as the working history or maintain two independently editable copies of one series.

Use JSONL for new user observations. Joint-source queries may use an agent-created [derived database](../../records/DATABASE.md) based on actual data; it does not replace sources. Establish units, semantics, and reconciliation rules for each new source. No fixed measurements, services, or workbook layout are prescribed. Preserve manual conflict resolutions and correction history during rebuilds.
