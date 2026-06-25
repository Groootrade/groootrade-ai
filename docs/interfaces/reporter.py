from abc import ABC, abstractmethod

class Reporter(ABC):

    @abstractmethod
    def generate(self, data):
        pass
