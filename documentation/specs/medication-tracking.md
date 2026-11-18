# Ongoing medication and supplement intake tracking

Count-based tracking from user reports. Other dosage forms require separate verification. Basis: [architecture](../ARCHITECTURE.md).

## Data separation
- Package/leaflet: unchanged source in raw; readable ingredients, form, quantities, and limitations in materials. product_information does not turn a supplement into a medicine. Describe an undated photo using the user's report date for the shown product; photo/manufacture dates remain unknown. Explicitly store this cataloging rationale.
- A clinician's recommendation is a separate prescription with its own source. Do not automatically attribute a user-selected combination to a particular clinician because its ingredients look similar.
- The actual reported regimen and intake progression form an ongoing course in records/medications, not another import directory. Its stable ID does not change with every report. A separate later course of the same product gets another ID.
- Historical outputs remain snapshots. Current intake facts do not replace clinicians' recommendations or vice versa.

## Storage
For ongoing use without a finite reported target, planned_duration_days and planned_total_units may be null. This means no duration was reported, not lifelong-use advice. Do not calculate totals from elapsed days. Store the known current regimen start in current_regimen_start_date, separately from an unknown start of all use. A year without day/month is start_period with year precision; never substitute January 1. Preserve earlier regimens with unknown durations as separate messages/descriptions with unknown boundaries.

HISTORY-*.json retains historical user information linked to materials/workbook cells and independent user clarifications. A workbook row date does not prove a dose-change date or a particular pill. Zeros/dashes do not prove discontinuation. Do not apply today's package composition automatically to all earlier doses/packages. Keep intake time/food relationship, manufacturer instructions, clinician prescription, and reported use separate. Preserve a user's correction assigning timing to another medication with its rationale; do not leave the erroneous regimen active. Extension verification: [architecture](../ARCHITECTURE.md).

COURSE-<id>.json describes product, material link, initial regimen, specified duration/target, user source, and log path. Time of day, confirmed start, clinician, and prescription may remain unknown. This structure targets count-based courses; other dosage forms need separate verification.

COURSE-<id>-events.jsonl contains one report per line with stable IDs. Each has effective_date (state/event date), recorded_date (registration date), source.kind: user_message, and an exact quotation. Unknown time does not become midnight. Times are not stored here; dates are local.

Supported events:
- checkpoint: reported_total_units as of effective_date. If last intake date is unknown, use last_intake_date: null. Optional expected_next stores a separately reported expectation.
- missed: user-confirmed missed intake with scheduled_units; taken count does not increase.
- regimen_change: reported units_per_day change, not a script recommendation to change dose.
- status_change: explicitly reported active, paused, stopped, completed. A calendar end date does not create completed.

Never overwrite old lines. Correct an erroneous cumulative count with a new checkpoint whose corrects_event_id references the previous checkpoint, with that checkpoint's effective_date, a new registration date, and a supporting quotation. The correction becomes visible on its registration date and replaces the old count at the corrected report's date. For older corrections with mismatched dates, use the original checkpoint date. If corrected totals decrease across checkpoints, verify the conflicting reports. Reject duplicate IDs and future confirmed events. Keep message text as evidence.

Append logs in receipt order, but reproduce state by effective_date, then recorded_date, preserving append order when both tie. A late-registered start does not cancel a later stop. An as-of view first filters by both dates; visible checkpoint corrections then exclude corrected entries from calculations without deleting history. Count-sequence verification uses the same event ordering.

## State and calendar
Store an intention to start as planned: date the plan event by the user message, with expected start in separate planned_start_date. Do not create future intake. Until the user explicitly confirms actual start, status stays planned even after expected start/end; pill counts do not increase. Label conditional course end separately. Basis: [architecture](../ARCHITECTURE.md).

Generate CURRENT.md from course definition and log as of an explicit date. Show the latest reported count and its report date; do not present it as today's automatically updated remaining supply. Future dates without new reports do not increase counts or set completion.

After regimen_change, the summary shows the date and dose from that report. Initial dose description, intake time, and food relationship remain in the course definition as information about the previous regimen.

Store a cumulative intake report as one checkpoint. If last intake date is unknown, show count and its effective reporting date. Conditional start/end projection requires a known last intake date.

The initial projection mechanism supports only one unit per day and an active course with no interruptions, missed intake, or regimen changes. Confirming the initial start of a planned course preserves eligibility once a qualifying checkpoint is recorded. Hide the projection after a pause even if the course resumes. Deviations require reconfirming the target.

## Commands
- `python scripts/medications.py verify` — validate definitions, sources, and logs.
- `python scripts/medications.py status --as-of YYYY-MM-DD` — JSON array of course states and separate REPORT messages. Reports registered by the as-of date appear as kind: user_report with path and report. --courses-only retains course-only output.
- `python scripts/medications.py render --as-of YYYY-MM-DD` — regenerate readable CURRENT.md.
- `python scripts/medications.py add-event COURSE_ID EVENT_JSON` — after reading the user's report and directory rules, append a prepared event. The script checks event validity and unchanged log contents before appending; run render separately with the required date.

## Verification and limits
Check unchanged reported counts on future dates, no automatic completion, and rejection of duplicate IDs, uncorrected decreases, and future confirmations. Missed intake disables projection; corrections retain earlier reports.

This is a local report-driven process, not a background service, reminders, or proof of adherence. Automation is not enabled. Concurrent writes from multiple processes and a database are not implemented. Total daily nutrient calculations, interactions, and clinical assessment belong to separate analysis, not intake registration.
