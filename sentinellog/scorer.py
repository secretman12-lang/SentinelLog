from enum import Enum
from typing import Dict


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"


def classify_risk(attempts: int) -> RiskLevel:
    """
    Classify risk level based on number of failed attempts.
    """

    if attempts <= 5:
        return RiskLevel.LOW
    if attempts <= 15:
        return RiskLevel.MEDIUM
    return RiskLevel.HIGH


def calculate_system_score(grouped: Dict[str, int]) -> int:
    """
    Calculate overall system risk score (0–100).
    """

    score = 0

    for attempts in grouped.values():
        if attempts <= 5:
            score += 1
        elif attempts <= 15:
            score += 5
        else:
            score += 10

    return min(score, 100)
