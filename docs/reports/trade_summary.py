from decision.trade_decision import TradeDecision

class TradeSummary:

    def display(self, trade: TradeDecision):

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        print("GroooTrade AI")

        print(f"Trade : {trade.trade_id}")

        print(f"Asset : {trade.symbol}")

        print(f"Timeframe : {trade.timeframe}")

        print()

        print(f"Decision : {trade.decision}")

        print(f"Confidence : {trade.confidence}%")

        print(f"Risk : {trade.risk_score}")

        print(f"Macro : {trade.macro_score}")

        print(f"Consensus : {trade.consensus}")

        print()

        print(f"Guardian : {'APPROVED' if trade.approved else 'REJECTED'}")

        print()

        print(f"Reason : {trade.reason}")

        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
