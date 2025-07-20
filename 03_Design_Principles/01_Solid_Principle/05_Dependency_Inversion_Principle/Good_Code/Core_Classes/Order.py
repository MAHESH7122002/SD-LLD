class Order:
    def __init__(self, id, product):
        self.id = id
        self.product = product 
        
    def get_id(self):
        return self.id 
    
    def get_product(self):
        return self.product