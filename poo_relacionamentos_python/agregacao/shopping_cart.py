class ShoppingCart:
    def __init__(self):
        self.__products = []
        
    @property
    def products(self):
        return self.__products
    
    
    def insert_product(self, product):
        self.__products.append(product)
        
    def list_all_product(self):
        for product in self.__products:
            print(product.__str__())
            
    def find_products_by_category(self, category_name):
        for product in self.__products:
            if product.category == category_name:
                print(product.__str__())
                
    def total_sum(self):
        total_sum_products = 0
        for product in self.__products:
            total_sum_products+= product.price
            
        return total_sum_products
        