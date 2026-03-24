from shopping_cart import ShoppingCart
from product import Product


shopping_cart = ShoppingCart()
product1 = Product(50, "Camisa", "Vestimenta")
product2 = Product(800, "Televisão", "Eletrodomestico")
product3 = Product(100, "Head-Set", "Periferico")
product4 = Product(300, "Calça", "Vestimenta")


shopping_cart.insert_product(product1)
shopping_cart.insert_product(product2)
shopping_cart.insert_product(product3)
shopping_cart.insert_product(product4)

shopping_cart.list_all_product()
print(shopping_cart.total_sum())
shopping_cart.find_products_by_category("Vestimenta")


