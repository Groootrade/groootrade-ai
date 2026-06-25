from market_analyzer import MarketAnalyzer
from trend_analyzer import TrendAnalyzer
from rsi_analyzer import RSIAnalyzer
from volume_analyzer import VolumeAnalyzer
from support_resistance import SupportResistance
from decision_brain import DecisionBrain


class BrainManager:

    def __init__(self):
        self.market = MarketAnalyzer()
        self.trend = TrendAnalyzer()
        self.rsi = RSIAnalyzer()
        self.volume = VolumeAnalyzer()
        self.levels = SupportResistance()
        self.decision = DecisionBrain()

    def analyze(self):

        self.market.analyze()

        self.trend.analyze_trend()

        self.rsi.analyze_rsi()

        self.volume.analyze_volume()

        self.levels.analyze_levels()

        self.decision.make_decision()

from brains.market_brain import MarketBrain
from brains.trend_brain import TrendBrain
from brains.rsi_brain import RSIBrain

class BrainManager:

    def run_analysis(self):

        market = MarketBrain()
        trend = TrendBrain()
        rsi = RSIBrain()

        market.analyze()
        trend.analyze()
        rsi.analyze()

        print("Analysis completed.")
votes = manager.run_analysis(market_data) [

    market.analyze(),

    trend.analyze(),

    rsi.analyze()

]

return votes
