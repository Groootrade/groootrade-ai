class RiskGuardian:

    def validate_trade(self, confidence):
        if confidence >= 95:
            print("High confidence trade")
        else:
            print("Trade rejected")
