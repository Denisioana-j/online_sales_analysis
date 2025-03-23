from product import Product
from product_manager import ProductManager
from cart import Cart

# Creăm managerul de produse și adăugăm produse
manager = ProductManager()
manager.add_product(Product("Laptop", 3500, 5))
manager.add_product(Product("Mouse", 100, 20))
manager.add_product(Product("Tastatură", 150, 15))

# Afișăm produsele din inventar
manager.display_products()
print(f"Total inventory value: {manager.total_inventory_value()} RON")

# Creăm un coș de cumpărături și adăugăm produse
cart = Cart()
cart.add_to_cart(manager.products[0])  # Laptop
cart.add_to_cart(manager.products[1])  # Mouse
cart.add_to_cart(manager.products[2])  # Tastatură

# Afișăm conținutul coșului și valoarea totală
print("\nProdusele din coș:")
cart.display_cart()
print(f"Total cart value: {cart.total_cart_value()} RON")
