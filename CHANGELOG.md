# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

---

## [0.1.1] - 2026-04-27

### Added

Full coverage of the 9 regimes across all 3 transformation families
(9 × 3 = 27 combinations), with one test case per combination.
All 27 cases execute and pass.

INH coverage for regimes that do not split (OBL, OCC, REC):

- These regimes do not define identity changes under any of the
  current transformation families.
- Tests confirm that for all three transformations (BF, decomposition,
  nor_reorg), the result is INH.
- This verifies that these regimes correctly do not engage their
  identity criteria under any transformation.

Cross-family negative tests for regimes that do split (12 cases):

- For each split regime (ENR, CTX, NOR), identity behavior is only
  defined for one transformation family.
- Additional tests cover the other transformation families where no
  split behavior is defined.
- These tests explicitly expect INH (no split pressure established).
- Purpose:
  - Confirms that identity is **not** evaluated where it should not be
  - Prevents accidental PRS or BRK results in those cases

Coverage breakdown:

- ENR-L, ENR-I tested under decomposition and nor_reorg (expect INH)
- CTX-E, CTX-S tested under BF and nor_reorg (expect INH)
- NOR-C, NOR-S tested under BF and decomposition (expect INH)

---

## [0.1.0] - 2026-04-27

### Added

- Initial release of `se-regimes-pilot-education-math-g8`

- Synthetic Grade 8 mathematics stress-test cases for SE regime behavior
  - ENR-L / ENR-I under `BF`
  - CTX-E / CTX-S under `decomposition`
  - NOR-C / NOR-S under `nor_reorg`
  - OBL, OCC, REC invariant (INH) coverage across all transformation families

- Complete regime x transformation coverage:
  - BF
  - decomposition
  - nor_reorg

- Stress report generation including:
  - rule matrix (registry-declared behavior)
  - case coverage matrix
  - per-case evaluation results

- `SE_MANIFEST.toml` repository declaration
- `CITATION.cff` citation metadata

- Minimal Python CLI for artifact inspection and report generation

- Documentation site (folder-based navigation)

- CI: GitHub Actions
  - lint
  - type check (pyright)
  - tests
  - docs build

- Repository hygiene
  - Ruff (lint + format)
  - pre-commit hooks

---

## Notes on versioning and releases

- We use **SemVer**:
  - **MAJOR** – breaking changes to artifact structure or validation semantics
  - **MINOR** – backward-compatible additions to schema or validation rules
  - **PATCH** – fixes, documentation, tooling
- Versions are driven by git tags. Tag `vx.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.
- Sample commands:

```shell
# as needed
git tag -d v0.1.1
git push origin :refs/tags/v0.1.1

# new tag / release
git tag v0.1.1 -m "0.1.1"
git push origin v0.1.1
```

[Unreleased]: https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/releases/tag/v0.1.1
[0.1.0]: https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/releases/tag/v0.1.0
