from collections import Counter
from typing import Dict, Iterable
from .parser import SSHFailureEvent


def group_failures_by_ip(events: Iterable[SSHFailureEvent]) -> Dict[str, int]:
    """
    Count failed attempts grouped by IP.
    """

    counter = Counter(event.ip for event in events)
    return dict(counter)
