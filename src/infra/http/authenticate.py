from typing import Generic
from domain.models.auth import UP
from ecase.auth import AuthManagerDependency
from infra.http.router.auth import get_auth_router

class UserAuthenticator(Generic[UP]):


    def __init__(self, get_user_manager: AuthManagerDependency[UP]):
        self.get_user_manager = get_user_manager

    
    def get_auth_router(self):
        
        return get_auth_router(
            self.get_user_manager
        )