from typing import TypeVar

ID = TypeVar("ID")


class  UserProtocolDB:

    def __init__(self, id:ID, email: str, hashed_password: str,
                 is_active:bool, is_superuser: bool, is_verified: bool):
        self.id = id 
        self.email = email
        self.hashed_password = hashed_password
        self.is_active = is_active
        self.is_superuser = is_superuser
        self.is_verified = is_verified

class UserProtocol():
    """ User Protocol that ORM mmodel should follow. """

    id: str 
    email: str 
    hashed_password:str 
    is_active: bool 
    is_superuser: bool 
    is_verified: bool 


UP = TypeVar("UP", bound=UserProtocol)