from market.market_snapshot import MarketSnapshot
from market.market_data import MarketData
from engine.trading_engine import TradingEngine

def main():

    snapshot = MarketSnapshot(
        symbol="EURUSD",
        price=1.1682,
        volume=25600,
        spread=0.2,
        timeframe="M15"
    )

    market = MarketData()
    market.update(snapshot)

    engine = TradingEngine()

    engine.execute(market)

if __name__ == "__main__":
    main()

from core.bootstrap import Bootstrap
from core.application import Application

def main():

    bootstrap = Bootstrap()

    container = bootstrap.build()

    app = Application(container)

    app.start()

if __name__ == "__main__":
    main()
