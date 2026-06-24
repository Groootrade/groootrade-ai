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
