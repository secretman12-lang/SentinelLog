import re
from dataclasses import dataclass
from typing import Iterable, List


IP_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


@dataclass
class SSHFailureEvent:
    ip: str
    raw_line: str


def parse_ssh_failures(lines: Iterable[str]) -> List[SSHFailureEvent]:
    """
    Extract SSH failed login attempts from log lines.
    """

    events: List[SSHFailureEvent] = []

    for line in lines:
        if "Failed password" not in line:
            continue

        match = IP_PATTERN.search(line)
        if match:
            events.append(
                SSHFailureEvent(
                    ip=match.group(),
                    raw_line=line.strip(),
                )
            )

    return events
