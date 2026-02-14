import re
from typing import List, Dict


IP_PATTERN = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")


def parse_ssh_failures(lines: List[str]) -> List[Dict]:
    events = []

    for line in lines:
        if "Failed password" in line:
            match = IP_PATTERN.search(line)
            if match:
                events.append({
                    "ip": match.group(),
                    "raw": line.strip()
                })

    return events
