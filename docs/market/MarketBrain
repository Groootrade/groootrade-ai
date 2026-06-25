from market.market_data import MarketData

class MarketBrain:

    def analyze(self, market_data):

        snapshot = market_data.get_snapshot()

        if snapshot is None:
            return "WAIT"

        if snapshot.spread > 3:
            return "WAIT"

        return "BUY"
