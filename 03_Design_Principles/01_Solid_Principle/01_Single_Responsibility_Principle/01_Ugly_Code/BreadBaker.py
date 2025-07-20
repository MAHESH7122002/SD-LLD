
class BreadBaker:
    def __init__(self):
        print("BreadBaker initialized")
    
    
    def bake_bread(self):
        print("Baking bread...")
        # Baking logic here
        print("Bread baked successfully!")
        
    def manage_Inventory(self):
        print("Managing inventory...")
        # Inventory management logic here
        print("Inventory managed successfully!")
        
    def clean_kitchen(self):
        print("Cleaning kitchen...")
        # Cleaning logic here
        print("Kitchen cleaned successfully!")
    
    def serve_bread(self):
        print("Serving bread...")
        # Serving logic here
        print("Bread served successfully!")
    
    def handle_customer_requests(self):
        print("Handling customer requests...")
        # Customer request handling logic here
        print("Customer requests handled successfully!")

#main
if __name__ == "__main__":
    baker = BreadBaker()
    baker.bake_bread()
    baker.manage_Inventory()
    baker.clean_kitchen()
    baker.serve_bread()
    baker.handle_customer_requests()