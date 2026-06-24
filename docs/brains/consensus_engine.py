class ConsensusEngine:

    def calculate_consensus(self):
        print("Calculating consensus...")

class ConsensusEngine:

    def calculate_consensus(self, votes):

        buy_votes = votes.count("BUY")
        sell_votes = votes.count("SELL")
        wait_votes = votes.count("WAIT")

        print(f"BUY: {buy_votes}")
        print(f"SELL: {sell_votes}")
        print(f"WAIT: {wait_votes}")

        return buy_votes, sell_votes, wait_votes
