class ConsensusEngine:

    def calculate_consensus(self, votes):

        buy_votes = votes.count("BUY")
        sell_votes = votes.count("SELL")
        wait_votes = votes.count("WAIT")

        if buy_votes > sell_votes and buy_votes > wait_votes:
            return "BUY"

        if sell_votes > buy_votes and sell_votes > wait_votes:
            return "SELL"

        return "WAIT"
