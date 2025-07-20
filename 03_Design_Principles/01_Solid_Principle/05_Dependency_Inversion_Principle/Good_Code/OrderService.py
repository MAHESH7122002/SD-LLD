from .Interfaces import NotificationService, LoggingService, InventoryService
from .Core_Classes.Order import Order

class OrderService:
    def __init__(self, notification_service: NotificationService, logging_service: LoggingService, inventory_service: InventoryService):
        self.notification_service = notification_service
        self.logging_service = logging_service
        self.inventory_service = inventory_service
        
    def place_order(self, order: Order):
        try:
            # Check inventory
            if self.inventory_service.check_availability(order.product):
                # Process order
                self.inventory_service.update_stock(order)
                # Send notification
                self.notification_service.send_notification(f"Order #{order.id} placed successfully")
                # Log success
                self.logging_service.log_message(f"Order processed successfully: {order.id}")
        except Exception as e:
            self.logging_service.log_error(f"Error processing order: {order.id} - {str(e)}")
            raise e
    def place_order(self, order):
        try:
            # Check inventory
            if self.inventory_service.check_availability(order.product):
                # Process order
                self.inventory_service.update_stock(order)
                # Send notification
                self.notification_service.send_notification(f"Order #{order.id} placed successfully")
                # Log success
                self.logging_service.log_message(f"Order processed successfully: {order.id}")
        except Exception as e:
            self.logging_service.log_error(f"Error processing order: {order.id} - {str(e)}")
            raise e