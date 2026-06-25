from abc import ABC, abstractmethod

class MarketProvider(ABC):

    @abstractmethod
    def get_snapshot(self, symbol, timeframe):
        pass
