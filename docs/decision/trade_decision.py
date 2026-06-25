from dataclasses import dataclass

@dataclass
class TradeDecision:

    trade_id: str

    symbol: str

    timeframe: str

    decision: str

    confidence: float

    risk_score: float

    macro_score: float

    consensus: str

    approved: bool

    reason: str
