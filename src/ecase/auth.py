from typing import Generic, Optional

from domain.models.auth import UP
from domain.services.db.base import BaseDatabase
from domain.services.password.pass_helper import PasswordService
from ecase.utils.types import DependencyCallable
from infra.helper.password import PasswordHelper

class AuthManager(Generic[UP]):

    def __init__(self, db_adapter: BaseDatabase, password_helper: Optional[PasswordService] = None):
        self.__db_adapter = db_adapter
        if password_helper is None:
            self.password_helper = PasswordHelper()
        else:
            self.password_helper = password_helper


    async def authenticate(
        self, credentials: UP
    ) -> Optional[UP]:
        """ 
        Authenticate and return a user following an email and a password.
        Will automatically upgrade password hash if necessary
        :param credentials: The user credentials
        """

        try:
            user = await self.__db_adapter.get_email(credentials.username)

        except ValueError as e:  # exceptions.UserNotExists
            pass 
        
        verified, updated_password_hash = self.password_helper.verify_and_update(
            plain_text=credentials.password, hashed_password=user.hashed_password
        )
        if not verified:
            return None 
        
        # Update password hash to a more robust one if needed
        if updated_password_hash is not None:
            await self.__db_adapter.update(user, {"hashed_password": updated_password_hash})

        return user


AuthManagerDependency = DependencyCallable[AuthManager[UP]]