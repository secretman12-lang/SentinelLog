import json
from typing import Dict

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from .scorer import classify_risk, calculate_system_score, RiskLevel


console = Console()


RISK_COLOR_MAP = {
    RiskLevel.LOW: "green",
    RiskLevel.MEDIUM: "yellow",
    RiskLevel.HIGH: "red",
}


def render_report(grouped: Dict[str, int]) -> None:
    """
    Render analysis results to terminal.
    """

    console.print(
        Panel.fit(
            "[bold cyan]SentinelLog[/bold cyan]\n"
            "SSH Security Analysis Report",
            border_style="cyan",
        )
    )

    if not grouped:
        console.print("[green]No suspicious activity detected.[/green]")
        return

    table = Table(title="Suspicious IP Activity")

    table.add_column("IP Address", style="cyan", no_wrap=True)
    table.add_column("Failed Attempts", justify="right")
    table.add_column("Risk Level", justify="center")

    for ip, attempts in sorted(grouped.items(), key=lambda x: x[1], reverse=True):
        risk = classify_risk(attempts)
        color = RISK_COLOR_MAP[risk]

        table.add_row(
            ip,
            str(attempts),
            f"[{color}]{risk.value}[/{color}]",
        )

    console.print(table)

    system_score = calculate_system_score(grouped)
    console.print(f"\n[bold]System Risk Score:[/bold] {system_score}/100")


def export_report_json(grouped: Dict[str, int], path: str) -> None:
    """
    Export analysis result to JSON file.
    """

    data = {
        "results": grouped,
        "system_score": calculate_system_score(grouped),
    }

    with open(path, "w") as f:
        json.dump(data, f, indent=4)
