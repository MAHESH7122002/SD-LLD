from abc import ABC, abstractmethod
class InventoryService(ABC):
    
    @abstractmethod
    def update_stock(self, order):
        pass
    
    @abstractmethod
    def check_availability(self, product):
        pass