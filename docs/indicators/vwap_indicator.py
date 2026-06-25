class VWAPIndicator:

    def analyze(self, price, vwap):

        if price > vwap:
            return "BUY"

        if price < vwap:
            return "SELL"

        return "WAIT"
