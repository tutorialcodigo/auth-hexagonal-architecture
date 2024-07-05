from abc import ABC, abstractmethod

class PasswordService(ABC):

    @abstractmethod
    def verify_and_update(self, plain_text:str, hashed_password: str):
        pass 

    @abstractmethod
    def hash(self, password:str):
        pass 
    
    @abstractmethod
    def generate(self):
        pass
        