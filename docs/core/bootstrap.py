from core.service_container import ServiceContainer

class Bootstrap:

    def build(self):

        container = ServiceContainer()

        return container

from providers.simulated_provider import SimulatedProvider

container.register(

    "market_provider",

    SimulatedProvider()

)
