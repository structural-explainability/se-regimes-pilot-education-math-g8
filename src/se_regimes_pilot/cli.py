"""cli.py - Command-line interface for se_regimes_pilot."""

import argparse
from pathlib import Path

from se_regimes_pilot.app import run_pilot_report, run_pilot_show


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser."""
    parser = argparse.ArgumentParser(
        prog="se_regimes_pilot",
        description="Evaluate SE regime stress-test cases: education mathematics grade 8.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    report_parser = subparsers.add_parser(
        "report",
        help="Evaluate all cases and write the stress report.",
    )
    report_parser.add_argument(
        "--cases",
        type=Path,
        default=None,
        help="Cases directory (default: ./cases).",
    )
    report_parser.add_argument(
        "--report",
        type=Path,
        default=None,
        help="Report output path (default: ./reports/stress_report.md).",
    )

    show_parser = subparsers.add_parser(
        "show",
        help="Show regime registry contents.",
    )
    show_parser.add_argument(
        "--kind",
        choices=["all", "regimes", "transformations"],
        default="all",
        help="Artifact subset to display.",
    )

    return parser


def main() -> int:
    """Run the command-line interface."""
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "report":
        return run_pilot_report(
            cases_dir=args.cases,
            report_path=args.report,
        )

    if args.command == "show":
        return run_pilot_show(kind=args.kind)

    parser.error(f"Unknown command: {args.command}")
    return 2
