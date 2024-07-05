from ecase.auth import AuthManager
from domain.models.auth import UP

from infra.http.router.auth import get_auth_router
from infra.http.authenticate import UserAuthenticator
from infra.cloud.conn import CloudServices
from infra.cloud.nosql import NoSql
from infra.helper.password import PasswordHelperProtocol, PasswordHelper

db =  CloudServices("dynamodb")
db_nosql = NoSql(conn=db.conn())

class UserManager(AuthManager):
    async def on_after_register(self):
        pass 

    async def on_after_forgot_password(self):
        pass 

async def  get_user_manager():
    yield UserManager(db_adapter=db_nosql)



fastapi_users =  UserAuthenticator[UP](get_user_manager=get_user_manager)