# Project decisions

Record the history of changes to architecture, formats, and operating rules here. [ARCHITECTURE.md](ARCHITECTURE.md) describes the current system.

No new decisions have been recorded. Before changing the approach, verify it in practice, then append a decision. Do not modify or delete earlier entries. Adding a document, measurement, or report under existing rules is not an architectural decision.

## New entry format
Use the next available number, starting at D-001. Add an explicit numeric anchor before the heading. Required fields: number, verifiable decision, rationale, and date. Include verification method and result boundaries when needed. Revisions reference an earlier decision or the architecture section they replace.

```markdown
<a id="1"></a>

## D-001 — Decision title

- **#**: 1.
- **Decision**: verifiable rule and its scope.
- **Rationale**: task, reason, and evidence for the approach.
- **Date**: YYYY-MM-DD.
- **Verification and limitations**: what was checked and what remains unknown.
```
