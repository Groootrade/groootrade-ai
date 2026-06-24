class GuardianManager:

    def approve_trade(self, confidence):

        if confidence < 70:
            print("Trade rejected.")
            return False

        print("Trade approved.")
        return True

class GuardianManager:

    def approve_trade(self, decision):

        if decision == "WAIT":
            print("Trade rejected.")
            return False

        print("Trade approved.")
        return True
