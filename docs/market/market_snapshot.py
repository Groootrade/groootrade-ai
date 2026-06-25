class MarketSnapshot:

    def __init__(self):

        self.symbol = "XAUUSD"

        self.price = 3350.25

        self.volume = 18542

        self.spread = 0.20

        self.timeframe = "M15"

class MarketSnapshot:

    def __init__(
        self,
        symbol,
        price,
        volume,
        spread,
        timeframe
    ):

        self.symbol = symbol
        self.price = price
        self.volume = volume
        self.spread = spread
        self.timeframe = timeframe
