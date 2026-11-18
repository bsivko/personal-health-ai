# Project state

## Capabilities
The material registry is empty. There are no observations, courses, consolidated facts, medical overview, database, or query results. This does not imply an absence of illness or treatment.

Shared operations are available for intake of previously verified materials, integrity checks and indexing, image viewing, XLSX extraction, medication-report tracking, and plotting. Commands and dependencies: [scripts/AGENTS.md](../scripts/AGENTS.md).

The agent creates document/export handlers in task context after examining the user's actual data. No ready-made integrations, service list, or mandatory source set is prescribed. Contract: [archives and exports](specs/archive-import.md).

This English edition uses English instructions, demonstrations, and generated report text. Source originals and exact quotations retain their original contents.

## Limitations
- Connect the model, OCR, speech recognition, and environment tools separately. There is no background service or calendar notification system.
- A new format requires handler verification. Keep each material's contents and verification limits in its card and registry entry.
- A derived database is optional. The agent determines schema and builder from sources and queries; check freshness and completeness before use.
- Medication tracking is limited to reported regimens and events. Count-based projections support one unit per day without gaps or changes. Concurrent writes by multiple processes are unsupported.
- Universal versioning and formats for new facts/measurements require verification when extended. Appointment package completeness depends on available data.
- File verification does not establish recognition accuracy or correctness of medical conclusions.

## Setup
Python 3.11+ for shared scripts. Optional dependencies are in [requirements.txt](../requirements.txt). Intake and updates run on request. There are no API keys or cloud-provider configurations. Determine timezone and provenance from the owner's sources. Verification commands: [CHECKS.md](CHECKS.md).
