class MarketData:

    def __init__(self):
        self.snapshot = None

    def update(self, snapshot):
        self.snapshot = snapshot

    def get_snapshot(self):
        return self.snapshot
