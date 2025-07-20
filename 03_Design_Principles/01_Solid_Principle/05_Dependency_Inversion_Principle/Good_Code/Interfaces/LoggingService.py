from abc import ABC, abstractmethod
class LoggingService(ABC):

    @abstractmethod
    def logMessage(self, message: str):
        pass

    @abstractmethod
    def logError(self, error: str):
        pass