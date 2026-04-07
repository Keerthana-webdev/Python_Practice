class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, qty):
        self.items[product] = self.items.get(product, 0) + qty

    def total_price(self):
        total = 0
        for product, qty in self.items.items():
            total += product.price * qty
        return total

    def apply_discount(self):
        total = self.total_price()
        return total * 0.9  # 10% discount
    
p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 500)

cart = Cart()

cart.add_product(p1, 1)
cart.add_product(p2, 2)

print("Total Price:", cart.total_price())
print("After Discount:", cart.apply_discount())