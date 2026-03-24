class Product:
    def __init__(self, price, name, category):
        self.__price = price
        self.__name = name
        self.__category = category
        
        
    @property 
    def price(self):
        return self.__price
    
    @property
    def name(self):
        return self.__name
    
    @property
    def category(self):
        return self.__category
    
    def __str__(self):
        return f"{", ".join([f'{key.split("__")[-1]}={value}' for key, value in self.__dict__.items()])}"