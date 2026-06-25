from indicators.rsi_indicator import RSIIndicator

class RSIBrain:

    def analyze(self):

        rsi = RSIIndicator()

        decision = rsi.calculate(27)

        return decision

from brains.brain_vote import BrainVote

class RSIBrain:

    def analyze(self, market):

        return BrainVote(

            brain_name="RSIBrain",

            decision="BUY",

            confidence=82,

            reason="RSI below 30"

        )
