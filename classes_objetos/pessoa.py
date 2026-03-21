# Criação da Classe Pessoa
class Pessoa:
    # Construtor em Python
    # self = Referência explicita para o objeto,Instancia do Objeto
    # self = Primeiro argumento explito
    def __init__(self,name,age):
        # Atributo para armazenar o nome
        self.name = name
        # Atributo par armazenar a idade
        self.age = age
        
    
    # Metodo para retornar uma apresentação
    def introduce_yourself(self):
        return f'Olá, meu nome é {self.name}!'
    
    
    # Metodo para exibir uma string persolanizada que representa o objeto
    def __str__(self):
        return f'{self.__class__.__name__}: {", ".join([f'{key}={value}' for key, value in self.__dict__.items()])}'
    
    
# Instancia da classe Pessoa
matheus = Pessoa("Matheus", 19)

# Exibição do retorno do metodo .introduce_yourself
print(matheus.introduce_yourself())

print("_________________________________________")

print(matheus.__str__())
    
    
       
        
        

                