class Processador:
    def __init__(self,model):
        self.__model = model
        
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, model_name):
        self.__model = model_name
        