from abc import ABC, abstractmethod


class BaseDatabase(ABC):

    @abstractmethod
    async def get(self, id:str):
        pass 

    @abstractmethod
    async def get_email(self, email:str):
        pass