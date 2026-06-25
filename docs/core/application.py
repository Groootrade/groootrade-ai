class Application:

    def __init__(self, container):

        self.container = container

    def start(self):

        print("Starting GroooTrade AI...")

provider = self.container.get("market_provider")

snapshot = provider.get_snapshot(

    "EURUSD",

    "M15"

)

print(snapshot)
