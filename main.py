from product import Product
from product_manager import ProductManager

manager = ProductManager()

# Adăugăm produse
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Mouse", 100, 20))
manager.add_product(Product("Tastatură", 150, 15))

# Afișăm produsele și valoarea totală a inventarului
manager.display_products()
print(f"Total inventory value: {manager.total_inventory_value()} RON")
