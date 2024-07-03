from domain.services.db.base import BaseDatabase

class NoSql(BaseDatabase):

    def __init__(self, conn):
        self.__conn = conn

    async def get(self, id:str):
        pass 

    async def get_email(self, email:str):
        pass

