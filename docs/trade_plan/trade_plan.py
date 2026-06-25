from dataclasses import dataclass

@dataclass
class TradePlan:

    symbol: str

    timeframe: str

    direction: str

    entry: float

    stop_loss: float

    take_profit: float

    risk_reward: float

    confidence: float

    reason: str
