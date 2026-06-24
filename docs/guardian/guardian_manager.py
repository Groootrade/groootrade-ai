class GuardianManager:

    def approve_trade(self, confidence):

        if confidence < 70:
            print("Trade rejected.")
            return False

        print("Trade approved.")
        return True
