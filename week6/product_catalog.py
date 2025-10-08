class Product_Catalog:
    def __init__(self, model, rating, type_of_UPS, quantity, price):
        self.model = model
        self.rating = rating
        self.type_of_UPS = type_of_UPS
        self.quantity = quantity
        self.price = price

    def product_list(self):
        print("Our Products\n")
        stock = (
            
            f"model: {self.model}\n"
            f"rating: {self.rating}\n"
            f"type of UPS: {self.type_of_UPS}\n"
            f"quantity: {self.quantity}\n"
            f"price: {self.price}"
        )
        return stock

    def availability_of_stock(self, amount):
        if self.quantity == 0:
            return f"Product {self.model} is out of stock"
        elif self.quantity < amount:
            return f"Sorry, only {self.quantity} {self.model} available. Continue with purchase? YES/NO" 
        elif self.quantity >= amount:
            return f"You ordered {amount} {self.model}"
        else:
            return "Invalid entry, try again"
    def total_value(self):
        total_product_value = int(self.quantity) * int(self.price)
        return total_product_value

class APC(Product_Catalog):
    def product_list(self):
        return super().product_list()

    def availability_of_stock(self, amount):
        return super().availability_of_stock(amount)

    def total_value(self):
        return super().total_value()
    
class VERTIV(Product_Catalog):
    def product_list(self):
        return super().product_list()

    def availability_of_stock(self, amount):
        return super().availability_of_stock(amount)
    

    def total_value(self):
        return super().total_value()
    
class EATON(Product_Catalog):
    def product_list(self):
        return super().product_list()

    def availability_of_stock(self, amount):
        return super().availability_of_stock(amount)

    def total_value(self):
        return super().total_value()

# Create product objects
Product = [
    APC("SRV", "1k", "ONLINE", 10, 100),
    APC("SRV2", "2k", "LINE-INTERACTIVE", 50, 110),
    APC("SRV3", "3k", "OFFLINE", 100, 20),

    VERTIV("V1", "2k", "ONLINE", 50, 110),
    VERTIV("V2", "2k", "LINE-INTERACTIVE", 50, 110),
    VERTIV("V3", "2k", "OFFLINE", 50, 110),

    EATON("E1", "2k", "ONLINE", 50, 110),
    EATON("E2", "2k", "LINE-INTERACTIVE", 50, 110),
    EATON("E3", "2k", "OFFLINE", 50, 110),
]

# Example usage
for p in Product:
    print(p.product_list())
    print(p.availability_of_stock(5))
    print(p.total_value())
    print("----")
