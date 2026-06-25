from dataclasses import dataclass

@dataclass
class DecisionContext:

    symbol: str

    timeframe: str

    market_snapshot: object

    indicators: dict

    economic_events: list

    sentiment: dict

    account_balance: float

    open_positions: int

    risk_percent: float
