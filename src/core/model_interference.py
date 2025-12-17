from abc import ABC, abstractmethod
#Enables abstraction
class ModelInterface(ABC):
#Base interface for all models
    @abstractmethod
    def train(self,x,y):
        pass
#Enforces training method   
    @abstractmethod
    def train(self,x):
        pass
#Enforces prediction method