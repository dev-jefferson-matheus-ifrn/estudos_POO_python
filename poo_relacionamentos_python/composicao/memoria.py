class MemoriaRam:
    def __init__(self, model, storage_ram):
        self.__model = model
        self.__storage_ram = storage_ram
        
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model):
        self.__model = model
        
        
    @property
    def storage_ram(self):
        return self.__storage_ram
    
    @storage_ram.setter
    def storage_ram(self, storage_ram):
        self.__storage_ram = storage_ram
        