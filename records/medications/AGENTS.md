# Ongoing medication intake tracking

Inherit `../AGENTS.md`.

- [CURRENT.md](CURRENT.md) — derived course state as of a stated date; generated from records, not edited manually.
- `COURSE-*.json` — stable course definition and product information source.
- `COURSE-*-events.jsonl` — intake reports and regimen/status changes; preserve old events and explicitly link corrections.
- `HISTORY-*.json` — historical user and workbook records with provenance; never infer an exact regimen-change timeline from row dates.
- `REPORT-*.json` — dated reports about following prescriptions, including courses not yet started; keep separate from confirmations of actual intake.
- A prescription, user regimen, confirmed intake, and projected calendar are distinct. Elapsed time does not confirm a pill was taken.
- Store intake date and message registration date separately. Do not expand "N taken" into N invented daily events.
- If the last intake date is unknown in a cumulative report, use `last_intake_date: null` in the checkpoint. Calendar projections require a known last intake date.
- Contract and commands: [intake tracking](../../documentation/specs/medication-tracking.md), [scripts](../../scripts/AGENTS.md).
