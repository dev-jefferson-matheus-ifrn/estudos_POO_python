class Digimon:
    def __init__(self, name, type, height, weight, description, battle_attack):
        self.name = name
        self.type = type
        self.height = height
        self.weight = weight
        self.description = description
        self.battle_attack = battle_attack
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
    def attack(self):
        return f'{self.name} atacou usando {self.battle_attack}'
    
    def get_description(self):
        return self.description
    
    
    
agumon = Digimon("Agumon","Dinossauro", 1.20, 50.0, "Agumon: Forma digievoluida de Koromon, é um digimon do tipo dinossauro calmo e gentil, seu ataque assinatura é o bafo de pimenta", "Bafo de Pimenta")


print(agumon.__str__())

print("____________________________")

print(agumon.get_description())

print("_____________________________")

print(agumon.attack())
        