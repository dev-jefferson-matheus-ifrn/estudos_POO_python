'''
O método destrutor sempre é executado quando uma instância é destruida. Destrutores em python não são tão necessários quanto em C++ porque o pyhton tem um coletor de lixo que lida com o gerenciamento de memória automaticamente. Para declarar o método destrutor da classe criamos um método com o nome __del__.
'''

class Cachorro:
    # Construtor da classe
    def __init__(self, name, race, weight, height):
        self.name = name
        self.race = race
        self.weight = weight
        self.height = height
        
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
    def bark(self):
        return 'AU AU!'
    
    # Destrutor da classe
    def __del__(self):
        pass
    
    
caramelo = Cachorro("Manteiga", "Golden", 50.0, 1.0)