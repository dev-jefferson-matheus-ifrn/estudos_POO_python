from animal import Animal
class Cachorro(Animal):
    
    def __init__(self, name, race, weight, height):
        self.name = name
        self.race = race
        self.weight = weight
        self.height = height
        
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
    def fazer_som(self):
        return "AU AU"
    

    
    
caramelo = Cachorro("Manteiga", "Golden", 50.0, 1.0)

print(caramelo.fazer_som())