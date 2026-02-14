import sys
import typer
from typing import Optional

from rich.console import Console

from .parser import parse_ssh_failures
from .analyzer import group_failures_by_ip
from .report import render_report, export_report_json


app = typer.Typer(
    help="SentinelLog - Professional SSH Log Analyzer",
    add_completion=False,
)

console = Console()


@app.command()
def analyze(
    file: Optional[str] = typer.Option(
        None,
        "--file",
        "-f",
        help="Path to SSH log file (if omitted, reads from STDIN).",
    ),
    export: Optional[str] = typer.Option(
        None,
        "--export",
        "-e",
        help="Export analysis result to JSON file.",
    ),
) -> None:
    """
    Analyze SSH log file for failed login attempts.
    """

    if file:
        try:
            with open(file, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            console.print("[bold red]Error:[/bold red] File not found.")
            raise typer.Exit(code=1)
    else:
        lines = sys.stdin.readlines()

    events = parse_ssh_failures(lines)
    grouped = group_failures_by_ip(events)

    render_report(grouped)

    if export:
        export_report_json(grouped, export)
        console.print(f"\n[green]Report exported to {export}[/green]")
