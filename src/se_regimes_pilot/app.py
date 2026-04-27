"""app.py - Application orchestration for se_regimes_pilot."""

from pathlib import Path

from se_regimes.app import run_report, run_show


def run_pilot_report(
    *, cases_dir: Path | None = None, report_path: Path | None = None
) -> int:
    """Evaluate all pilot cases and write the stress report."""
    repo_root = Path.cwd()
    cases_dir = cases_dir or repo_root / "cases" / "education" / "math" / "g8"
    report_path = report_path or repo_root / "reports" / "stress_report.md"
    return run_report(cases_dir=cases_dir, report_path=report_path)


def run_pilot_show(*, kind: str = "all") -> int:
    """Show regime registry contents."""
    return run_show(kind=kind)
