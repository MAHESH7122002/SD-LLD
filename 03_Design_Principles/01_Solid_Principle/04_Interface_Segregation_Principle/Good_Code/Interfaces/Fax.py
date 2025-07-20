from abc import ABC, abstractmethod

class Fax(ABC):
    @abstractmethod
    def fax(self):
        pass
