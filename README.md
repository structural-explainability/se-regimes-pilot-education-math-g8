# se-regimes-pilot-education-math-g8

[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://structural-explainability.github.io/se-regimes-pilot-education-math-g8/)
[![Repo](https://img.shields.io/badge/repo-GitHub-black?logo=github)](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8)
[![Python 3.15+](https://img.shields.io/badge/python-3.15%2B-blue?logo=python)](./pyproject.toml)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](./LICENSE)

[![CI](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/structural-explainability/se-regimes-pilot-education-math-g8/actions/workflows/links.yml)

> Grade 8 mathematics stress-test cases used to verify how
> Structural Explainability regimes behave under different transformations.

## Owns

- `cases/education/math/g8/` - domain stress-test cases for Grade 8 mathematics

## Includes

### Stress-test cases

Each regime defines how identity behaves
under a specific type of transformation.

- ENR-L, ENR-I: locus vs. instance identity under branching
- CTX-E, CTX-S: extensional vs. structural context under decomposition
- NOR-C, NOR-S: content vs. structural normative identity under reorganization
- OBL, OCC, REC: unsplit regime coverage cases

### Coverage report

- regime × transformation family coverage matrix
- per-case pass/fail results
- complete coverage of all regime–transformation combinations (9 × 3)

### Depends on

- `se-regimes` - regime registry and engine

## Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```shell
git clone https://github.com/structural-explainability/se-regimes-pilot-education-math-g8

cd se-regimes-pilot-education-math-g8
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.15
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install

git add -A
uvx pre-commit run --all-files
# repeat if changes were made
git add -A
uvx pre-commit run --all-files

# run the module (core registry / theory & rules)
uv run python -m se_regimes.registry
uv run python -m se_regimes show

# run pilot stress report (cases / evidence)
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

</details>

## Citation

[CITATION.cff](./CITATION.cff)

## License

[LICENSE](./LICENSE)

## Manifest

[SE_MANIFEST.toml](./SE_MANIFEST.toml)
