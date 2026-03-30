from abc import ABC, abstractmethod

class Animal(ABC):

    def dormir(self):
        return "Dormindo..."

    @abstractmethod
    def fazer_som(self):
        pass