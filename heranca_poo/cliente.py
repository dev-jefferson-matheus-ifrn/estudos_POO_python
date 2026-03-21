class Cliente:
    def __init__(self,country,data_register):
        self.country = country
        self.data_register = data_register
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{key}={value}' for key, value in self.__dict__.items()])}'
        