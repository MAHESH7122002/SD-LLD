
from BreadBaker import BreadBaker
from InventoryManager import InventoryManager
from SupplyOrder import SupplyOrder
from CustomerService import CustomerService
from BakeryCleaner import BakeryCleaner


class Bakery:
    def __init__(self):
        print("Bakery initialized")
    
    def main(self):
        baker = BreadBaker()
        inventory_manager = InventoryManager()
        supply_order = SupplyOrder()
        customer_service = CustomerService()
        cleaner = BakeryCleaner()
        
        # Each class focuses on its specific responsibility
        baker.bake_bread()
        inventory_manager.manage_inventory()
        supply_order.orderSupplies()
        customer_service.serve_customer()
        cleaner.cleanBakery()


# main
if __name__ == "__main__":
    bakery = Bakery()
    bakery.main()