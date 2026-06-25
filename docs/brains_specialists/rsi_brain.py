from indicators.rsi_indicator import RSIIndicator

class RSIBrain:

    def analyze(self):

        rsi = RSIIndicator()

        decision = rsi.calculate(27)

        return decision
