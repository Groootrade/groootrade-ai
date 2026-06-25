class RSIIndicator:

    def calculate(self, value):

        if value < 30:
            return "BUY"

        if value > 70:
            return "SELL"

        return "WAIT"
