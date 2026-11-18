# Project documentation

## Reading and rule priority
Before the first changes in a branch, read this file and [ARCHITECTURE.md](ARCHITECTURE.md). To understand the system, make decisions, resolve contradictions, or extend the project, read the current architecture and affected contracts. When revising, check the relevant decisions in the log.

Active descriptions must follow these rules; preserve decision history in DECISIONS.

## Structure
All paths below are relative to documentation/.
- [DECISIONS.md](DECISIONS.md) — chronological decision history: "Why this way?"
- [ARCHITECTURE.md](ARCHITECTURE.md) — current architecture only: "How is it structured?"
- [CURRENT.md](CURRENT.md) — capabilities, limitations, and open questions.
- [REQUIREMENTS.md](REQUIREMENTS.md) — user scenarios and result criteria.
- [specs/AGENTS.md](specs/AGENTS.md) — operation contract navigation.

## DECISIONS
The log is append-only: each new decision is a section at the end. Do not delete or rewrite previous entries or retroactively annotate them as revoked ([architecture](ARCHITECTURE.md)).

Required fields:
- **#** — sequential number. Start with D-001 and continue the sequence. The heading contains the D-number; this field contains its numeric part. Add an explicit numeric anchor before the section for links such as `DECISIONS.md#40`.
- **Decision** — a verifiable rule with boundaries of allowed and prohibited behavior.
- **Rationale** — the source and reason for the decision.
- **Date** — adoption date.

Include context, verification method, and limits of confirmation when useful for assessing the decision. Do not present unverified assumptions as confirmed results.

Record revisions as new decisions referencing the previous number or superseded architecture section. Old text remains historical; ARCHITECTURE reflects current state. Repeat the most important active decisions in the relevant AGENTS.md as mandatory rules with decision references. Do not move discussion history, operations, or rationale there ([architecture](ARCHITECTURE.md)).

Routine intake of materials, measurements, or medication reports is not a new architectural decision.

## ARCHITECTURE
A snapshot of the current system organized by topic, without history or rationale. Those belong in DECISIONS ([architecture](ARCHITECTURE.md)).

Update it when system content changes: layers, documents, requirements, external contracts, or extracted functionality. Rewrite changed descriptions in place; remove or replace superseded text rather than appending competing descriptions. Git and DECISIONS retain history; the read-only git rule remains in force.

After adopting or revising a decision, align architecture, affected contracts, and operating rules. Describe detailed formats in specifications and link to them from architecture.

## Other rules
- Medical state belongs in `../overview/`; project state in documentation.
- Avoid duplicating detailed information between files; link to the responsible document.
- Do not maintain aggregate counters of materials, files, pages, or measurements. CURRENT describes capabilities and limitations, not intake history; update it when those change. Keep material details in cards and the manifest ([architecture](ARCHITECTURE.md)).
- Specifications define results and verification. Test a new approach through a proof of concept or another suitable method; preserve verification boundaries in the decision.
