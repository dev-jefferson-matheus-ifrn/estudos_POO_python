from cliente import Cliente

class Pessoa_fisica(Cliente):
    def __init__(self, country, data_register, name, last_name, cpf):
        super().__init__(country, data_register)
        
        self.name = name
        self.last_name = last_name
        self.cpf = cpf