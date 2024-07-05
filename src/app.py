from infra.server import fastapi_users

from fastapi import FastAPI

app = FastAPI()


app.include_router(   
    fastapi_users.get_auth_router(),
    prefix="/auth/jwt",
    tags=["auth"]
)


