# Devin Instructions for gb-load-calc

You are helping build a GB electrical load calculation tool (mainly GB 50054).

## Behavior
- Write clear, commented Python code.
- Prefer simple, testable functions over complex architecture.
- Always cite the relevant GB clause when applying a rule (e.g. "GB 50054-2011 6.2.2" or "per ampacity table in GB 50054").
- Open a PR for every meaningful change. Title format: `[feat/fix] short description`.
- Include a short summary of what changed and which GB rules were applied.
- Add or update unit tests for any calculation logic.

## Core requirements
- Support ambient temperature derating.
- Distinguish continuous vs non-continuous loads.
- Handle motor starting current (typically 6–8×) for protection checks.
- Flag when calculated load exceeds cable ampacity after derating.
- Keep rule tables in JSON for easy update.

## PR checklist
- [ ] Tests added/updated
- [ ] GB clause cited in comments or commit message
- [ ] No hardcoded magic numbers without explanation
