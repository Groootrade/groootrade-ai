from dataclasses import dataclass

@dataclass
class CouncilMember:

    name: str

    decision: str

    confidence: float

    reason: str
