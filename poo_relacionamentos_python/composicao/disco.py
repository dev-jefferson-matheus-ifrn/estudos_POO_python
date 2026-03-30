class Disco:
    def __init__(self, type, storage):
        self.__type = type
        self.__storage = storage
        
    @property
    def type(self):
        return self.__type
    
    @type.setter
    def type(self, type):
        self.__type = type
        
        
    @property
    def storage(self):
        return self.__storage
    
    @storage.setter
    def storage(self, storage):
        self.__storage = storage
        