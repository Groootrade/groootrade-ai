class Vote:

    BUY = 1
    SELL = -1
    WAIT = 0

from dataclasses import dataclass

@dataclass
class BrainVote:

    brain_name: str

    decision: str

    confidence: float

    reason: str
