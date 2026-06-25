from market.market_snapshot import MarketSnapshot
from providers.market_provider import MarketProvider

class SimulatedProvider(MarketProvider):

    def get_snapshot(self, symbol, timeframe):

        return MarketSnapshot(

            symbol=symbol,

            timeframe=timeframe,

            price=1.1682,

            volume=25480,

            spread=0.2
        )
