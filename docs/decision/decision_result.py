from dataclasses import dataclass

@dataclass
class DecisionResult:

    approved: bool

    decision: str

    confidence: float

    reasons_for: list

    reasons_against: list

    warnings: list
