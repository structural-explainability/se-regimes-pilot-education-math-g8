"""tests/test_cli.py - Minimal CLI smoke tests for se_regimes_pilot."""

from pathlib import Path

from se_regimes_pilot.app import run_pilot_report, run_pilot_show


def test_run_pilot_show_returns_success() -> None:
    """run_pilot_show should return 0 for default invocation."""
    rc = run_pilot_show(kind="all")
    assert rc == 0


def test_run_pilot_report_returns_success(tmp_path: Path) -> None:
    """run_pilot_report should evaluate bundled cases and write a report."""
    report_path = tmp_path / "stress_report.md"

    rc = run_pilot_report(report_path=report_path)

    assert rc == 0
    assert report_path.exists()
