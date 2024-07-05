from typing import Tuple

from domain.models.auth import UP
from ecase.auth import AuthManager, AuthManagerDependency

from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordRequestForm
from infra.utils.common import ErrorCode, ErrorModel

def get_auth_router(
    get_user_manager: AuthManagerDependency,
    requires_verification: bool = False 
) -> APIRouter:
    """Generate a router with login/logout routes for an authentication backend."""
    router = APIRouter()

    login_response = {
        status.HTTP_400_BAD_REQUEST: {
            "model": ErrorModel,
            "content": {
                "application/json": {
                    "examples": {
                        ErrorCode.LOGIN_BAD_CREDENTIALS: {
                            "summar": "Bad credentials or the user is inactive",
                            "value":  {"detail": ErrorCode.LOGIN_BAD_CREDENTIALS},
                        },
                    },
                }
            }
        }
    }
    @router.post(
        "/login",
        name=f"auth:login",
        responses=login_response, 
    )
    async def login(
        request: Request,
        credentials: OAuth2PasswordRequestForm = Depends(),
        user_manager: AuthManager[UP] = Depends(get_user_manager)
    ):
        
        user = await user_manager.authenticate(credentials)

        if user is None or not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.LOGIN_BAD_CREDENTIALS
            )
        
        if requires_verification and not user.is_verified:
            raise HTTPException(
                status=status.HTTP_400_BAD_REQUEST,
                detail=ErrorCode.LOGIN_USER_NOT_VERIFIED
            )
        

        return user
    
    @router.post("/logout")
    async def logout():
        pass
        
    
    return router

