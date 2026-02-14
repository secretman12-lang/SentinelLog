from sentinellog.parser import parse_ssh_failures


def test_parse_ssh():
    lines = [
        "Failed password for root from 1.1.1.1 port 22 ssh2"
    ]

    events = parse_ssh_failures(lines)

    assert len(events) == 1
    assert events[0].ip == "1.1.1.1"
