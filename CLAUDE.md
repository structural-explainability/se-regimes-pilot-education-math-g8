# CLAUDE.md (se-regimes-pilot-education-math-g8)

## Agent instructions

Follow repository-wide constraints defined in `AGENTS.md`.

## Purpose

Stress-test case suite for Structural Explainability identity and persistence regimes
applied to Grade 8 mathematics education standards.

Depends on `se-regimes` for the regime registry, transformation families, and engine.
This repo owns only the domain case files under `cases/education/math/g8/`.

## Commands (uv-only; see AGENTS.md)

```shell
uv run python -m se_regimes_pilot report

# do chores
npx markdownlint-cli "**/*.md" --fix
uv run python -m ruff format .
uv run python -m ruff check . --fix
uv run python -m pyright
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

## Key files

| File                       | Purpose                               |
| -------------------------- | ------------------------------------- |
| `cases/education/math/g8/` | Domain stress-test cases (TOML)       |
| `reports/stress_report.md` | Generated coverage and failure report |

## Case file rules

- Each `[[case]]` entry declares:
  - `id`, `domain`, `description`, `candidate_regime`,
  - `transformations`, `expected`, `notes`.
- `domain` must be `education.math.g8` for all cases in this suite.
- Case IDs must be unique across all files.
- `expected` entries declare `after`, `regime`, `outcome` (PRS or BRK).

## Dependency

```toml
[tool.uv.sources]
se-regimes = { git = "https://github.com/structural-explainability/se-regimes" }
```
