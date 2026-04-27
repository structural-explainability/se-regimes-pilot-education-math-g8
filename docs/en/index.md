# Structural Explainability Regimes Pilot Education Math Grade 8

This repository contains stress-test cases for
Structural Explainability (SE) identity and persistence regimes
applied to Grade 8 mathematics.

## Purpose

- Provide domain-grounded test cases for all 9 SE regime profiles
- Exercise all transformation families (branching, decomposition, normative reorganization)
- Generate a stress report showing:
  - declared regime responses (PRS / BRK / INH)
  - case coverage (regime x transformation)
  - per-case pass/fail outcomes

This repository does not define regimes or transformations.
It uses the canonical definitions from `se-regimes`.

## Scope

Domain: `education.math.g8`

Includes:

- linear equations (one variable, two-sided)
- proportional reasoning
- introductory statistical contexts

Excludes:

- regime definitions (owned by `se-regimes`)
- transformation definitions (owned by `se-regimes`)
- mapping validation or schema enforcement
- domains outside Grade 8 mathematics

## How it works

1. Cases are declared in TOML under `cases/education/math/g8/`
2. Each case specifies:
   - candidate regime
   - transformation family
   - expected outcome (PRS or BRK)
3. The engine evaluates each case against the regime registry
4. A stress report is generated

## Running the pilot

```shell
uv run python -m se_regimes_pilot report
```

Optional:

```shell
uv run python -m se_regimes_pilot report \
  --cases cases/ \
  --report reports/stress_report.md
```

## Output

The generated report includes:

- Rule matrix (registry-declared responses)
- Case coverage matrix
- Per-case results
- Failure diagnostics (if any)

## Relationship to other repositories

- `se-regimes` — canonical regime registry and evaluation engine
- `se-mapping-education-math-g8` — source mapping artifacts (referenced for traceability only)

This repository acts as a regime validation layer, not a mapping validator.

## Design principles

- Declarative cases (TOML only; no embedded logic)
- Deterministic evaluation
- Clear separation between:
  - regime theory
  - domain examples
  - mapping artifacts
- No hidden coupling to external data sources

## Status

Active pilot with initial coverage across all regime families.
