from abc import ABC, abstractmethod

class Brain(ABC):

    @abstractmethod
    def analyze(self, context):
        pass
