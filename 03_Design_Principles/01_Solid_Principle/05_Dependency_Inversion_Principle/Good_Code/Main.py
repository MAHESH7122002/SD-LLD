from .Concrete_Loggers.DatabaseLogger import DatabaseLogger
from .Concrete_Notifiers.EmailNotifier import EmailNotifier, PushNotifier, SMSNotifier
from .Concrete_Inventories import WarehouseInventoryService
import OrderService
class Main:
    def main():
        # Usage with dependency injection
        email_notifier = EmailNotifier()
        logger = DatabaseLogger()
        inventory = WarehouseInventoryService()
        order_service = OrderService(email_notifier, logger, inventory)

    if __name__ == "__main__":
        main()