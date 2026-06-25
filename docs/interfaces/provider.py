from abc import ABC, abstractmethod

class Provider(ABC):

    @abstractmethod
    def fetch(self):
        pass
