class TradingEngine:

    def start(self):
        print("GroooTrade AI started.")

    def analyze_market(self):
        print("Analyzing market...")

    def request_decision(self):
        print("Requesting decision from brains...")

from brains.brain_manager import BrainManager

class TradingEngine:

    def analyze_market(self):

        manager = BrainManager()

        manager.run_analysis()

        print("Market analysis completed.")

from brains.master_brain import MasterBrain
from guardian.guardian_manager import GuardianManager

class TradingEngine:

    def execute(self):

        master = MasterBrain()

        decision = master.make_decision()

        guardian = GuardianManager()

        approved = guardian.approve_trade(decision)

        if approved:
            print("Trade execution authorized.")
        else:
            print("Trade execution blocked.")

market = MarketData()

snapshot = MarketSnapshot(
    "EURUSD",
    1.1682,
    25600,
    0.2,
    "M15"
)

market.update(snapshot)

decision = market_brain.analyze(market)
