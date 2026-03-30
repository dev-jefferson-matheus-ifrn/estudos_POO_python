from processador import Processador
from memoria import MemoriaRam
from disco import Disco
class Computador:
    def __init__(self, model_processor, model_ram, storage_ram, type_disc, storage_disc):
        self.__model_processor = Processador(model_processor)
        self.__ram_memory = MemoriaRam(model_ram, storage_ram)
        self.__disk = Disco(type_disc, storage_disc)
        
        
    @property
    def model_processor(self):
        return self.__model_processor
    
    
    @property
    def ram_memory(self):
        return self.__ram_memory
    
    
    @property
    def disk(self):
        return self.__disk
    
    
    def list_especifications(self):
        print(f"Especificações Do Computador\n {self.model_processor.model}\n{self.__disk.type, self.__disk.storage}\n{self.__ram_memory.model, self.__ram_memory.storage_ram}")

    