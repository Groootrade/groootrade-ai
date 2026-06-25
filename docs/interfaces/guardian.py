from abc import ABC, abstractmethod

class Guardian(ABC):

    @abstractmethod
    def validate(self, decision):
        pass
