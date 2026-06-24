class MasterBrain:

    def gather_votes(self):
        print("Gathering votes from all brains...")

    def request_consensus(self):
        print("Building consensus...")

    def request_guardians(self):
        print("Requesting guardians approval...")

class MasterBrain:

    def make_decision(self):

        print("Collecting brains opinions...")
        print("Building consensus...")
        print("Decision generated.")

from brains.consensus_engine import ConsensusEngine

class MasterBrain:

    def make_decision(self):

        votes = [
            "BUY",
            "BUY",
            "WAIT"
        ]

        consensus = ConsensusEngine()

        result = consensus.calculate_consensus(votes)

        print(result)
