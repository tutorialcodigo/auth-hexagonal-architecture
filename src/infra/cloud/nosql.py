from domain.services.db.base import BaseDatabase
from domain.models.auth import UserProtocolDB

from typing import Optional

class NoSql(BaseDatabase):

    def __init__(self, conn):
        self.__conn = conn

    async def get(self, id:str):
        pass 

    async def get_email(self, email:str) -> Optional[UserProtocolDB]:

        print("get email: ", email)

        return UserProtocolDB(

            id="id-12345678", 
            email="fake@gmail.com",
            hashed_password="$argon2id$v=19$m=65536,t=3,p=4$6Bn4kUpqG372eiI6tHlUwg$v5x/XUqKsLgrJqoeWcISJBMkTC+MahR9higyq/8ZE4Q",
            is_active=True,
            is_superuser=False,
            is_verified=False
        )

    async def update(self, email:str):
        pass

