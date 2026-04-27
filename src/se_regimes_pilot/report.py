"""se_regimes_pilot.report - (math g8) Render stress_report.md from engine results.

Run from root folder with:

# evaluate cases, write reports/stress_report.md
uv run python -m se_regimes_pilot report

# optional explicit paths
uv run python -m se_regimes_pilot report --cases cases/ --report reports/stress_report.md

"""

from pathlib import Path

from se_regimes.engine import CaseResult
from se_regimes.registry import Registry


def write_report(
    path: Path,
    results: list[CaseResult],
    coverage: dict[str, dict[str, list[str]]],
    registry: Registry,
    reg_warnings: list[str],
) -> None:
    """Write a markdown report to the given path, summarizing the results and coverage."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lines: list[str] = []

    passed = sum(1 for r in results if r.passed)
    failed = sum(1 for r in results if not r.passed)
    family_ids = list(registry.families.keys())

    lines += [
        "# se-regimes-pilot-edu-math-g8 stress report",
        "",
        f"**Regimes:** {len(registry.regimes)}  "
        f"**Families:** {len(registry.families)}  "
        f"**Cases:** {len(results)}  "
        f"**Passed:** {passed}  "
        f"**Failed:** {failed}",
        "",
    ]

    if reg_warnings:
        lines += ["## Registry warnings", ""]
        for w in reg_warnings:
            lines.append(f"- {w}")
        lines.append("")

    # Coverage matrix
    lines += ["## Coverage matrix", ""]
    header = "| regime |" + "".join(f" {fid} |" for fid in family_ids)
    sep = "| --- |" + "".join(" --- |" for _ in family_ids)
    lines += [header, sep]
    for rid in registry.regimes:
        row = f"| `{rid}` |"
        for fid in family_ids:
            cell = coverage[rid][fid]
            row += f" {'✓' if cell else '-'} |"
        lines.append(row)
    lines.append("")

    # Failures
    if failed:
        lines += ["## Failures", ""]
        for r in results:
            if not r.passed:
                lines.append(f"### {r.case.id}")
                lines.append(f"- domain: `{r.case.domain}`")
                lines.append(f"- candidate_regime: `{r.case.candidate_regime}`")
                lines.append(f"- description: {r.case.description}")
                for msg in r.failures:
                    lines.append(f"- **{msg}**")
                lines.append("")

    # All results
    lines += ["## All cases", ""]
    lines.append("| id | domain | regime | result |")
    lines.append("| --- | --- | --- | --- |")
    for r in results:
        status = "✓" if r.passed else "✗"
        lines.append(
            f"| `{r.case.id}` | `{r.case.domain}` | `{r.case.candidate_regime}` | {status} |"
        )

    path.write_text("\n".join(lines) + "\n")
