from cliente import Cliente

class Pessoa_juridica(Cliente):
    def __init__(self, country, data_register, social_reason, name_fantasy, acronym, cnpj):
        super().__init__(country, data_register)
        
        self.social_reason = social_reason
        self.name_fantasy = name_fantasy
        self.acronym = acronym
        self.cnpj = cnpj