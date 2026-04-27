# Changelog

<!-- markdownlint-disable MD024 -->

All notable changes to this project will be documented in this file.

The format is based on **[Keep a Changelog](https://keepachangelog.com/en/1.1.0/)**
and this project adheres to **[Semantic Versioning](https://semver.org/spec/v2.0.0.html)**.

## [Unreleased]

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
- Versions are driven by git tags. Tag `vX.Y.Z` to release.
- Docs are deployed per version tag and aliased to **latest**.
- Sample commands:

```shell
# as needed
git tag -d v0.1.0
git push origin :refs/tags/v0.1.0

# new tag / release
git tag v0.1.0 -m "0.1.0"
git push origin v0.1.0
```

[Unreleased]: https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/releases/tag/v0.1.0
