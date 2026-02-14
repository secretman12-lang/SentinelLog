
---

# 🛡️ SentinelLog

> Professional SSH Log Analyzer for detecting suspicious authentication activity.

SentinelLog is a modular and extensible CLI tool designed to analyze SSH authentication logs and identify suspicious login behavior based on failed password attempts.

It follows clean architecture principles, strong typing practices, and modern Python packaging standards.

---

## 🚀 Features

* 🔍 Detects SSH failed login attempts
* 📊 Aggregates suspicious activity by IP address
* 🎯 Risk classification (LOW / MEDIUM / HIGH)
* 📈 System-wide risk scoring (0–100)
* 🖥 Rich-based terminal interface
* 📤 JSON export support
* 📥 STDIN support (pipeline compatible)
* 🧩 Modular architecture (parser → analyzer → scorer → report)
* 📦 Installable CLI tool via `pip`

---

## 📦 Installation

### Clone the repository

```bash
git clone https://github.com/your-username/SentinelLog.git
cd SentinelLog
```

### Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install locally (editable mode)

```bash
pip install -e .
```

You can now run:

```bash
sentinellog --help
```

---

## 🧠 Usage

### Analyze SSH log file

```bash
sentinellog --file /var/log/auth.log
```

### Analyze custom log file

```bash
sentinellog --file sentinellog/auth.log
```

### Export analysis report

```bash
sentinellog --file auth.log --export report.json
```

### Use with STDIN

```bash
cat auth.log | sentinellog
```

---

## 📊 Example Output

```
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
┃ IP Address   ┃ Failed Attempts ┃ Risk Level ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
│ 192.168.0.45 │               2 │    LOW     │
│ 10.0.0.8     │               1 │    LOW     │
└──────────────┴─────────────────┴────────────┘

System Risk Score: 2/100
```

---

## 🏗 Architecture

```
sentinellog/
├── cli.py        # CLI entry point
├── parser.py     # Extracts SSH failure events
├── analyzer.py   # Groups events by IP
├── scorer.py     # Risk modeling & scoring logic
├── report.py     # Terminal rendering & JSON export
```

Design principles:

* Separation of concerns
* Typed interfaces
* Extensible detection pipeline
* Clear responsibility boundaries

---

## 🔐 Risk Classification Model

| Failed Attempts | Risk Level |
| --------------- | ---------- |
| 0–5             | LOW        |
| 6–15            | MEDIUM     |
| 16+             | HIGH       |

The overall system score is calculated based on aggregated suspicious activity across all detected IP addresses.

---

## 🧪 Testing

```bash
pytest
```

(Tests can be extended for parser accuracy, risk classification, and score calculation.)

---

## 🛠 Tech Stack

* Python 3.10+
* Typer (CLI framework)
* Rich (terminal rendering)
* Dataclasses
* Enum-based risk modeling
* PEP 621 packaging (`pyproject.toml`)

---

## 🎯 Roadmap

* [ ] Multi-log support (Apache / Nginx)
* [ ] Time-based anomaly detection
* [ ] Configurable thresholds
* [ ] Real-time monitoring mode
* [ ] Plugin-based detector architecture
* [ ] Docker image
* [ ] CI/CD integration

---

## 📄 License

MIT License

---