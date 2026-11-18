# Project decisions

Record the history of changes to architecture, formats, and operating rules here. [ARCHITECTURE.md](ARCHITECTURE.md) describes the current system.

Before changing the approach, verify it in practice, then append a decision. Do not modify or delete earlier entries. Adding a document, measurement, or report under existing rules is not an architectural decision.

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

<a id="1"></a>

## D-001 — Preserve source and material bytes in Git

- **#**: 1.
- **Decision**: Disable Git line-ending conversion for all files in `incoming/`, `raw/`, and `materials/`. Keep LF normalization for the fictional fixtures.
- **Rationale**: A text original with CRLF endings can acquire a different checksum after a Git round trip. Registered derived files also rely on exact byte checksums.
- **Date**: 2026-11-19.
- **Verification and limitations**: Reproduced the original mismatch and checked Git's input and checkout filters on fictional files with `core.autocrlf` set to `true`, `false`, and `input`. The attributes apply to future Git operations. Recovery of previously normalized originals requires a copy with the original bytes.
