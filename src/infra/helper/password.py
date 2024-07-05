from domain.services.password.pass_helper import PasswordService

import secrets
from typing import Optional, Protocol, Tuple, Union
from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher

class PasswordHelperProtocol(Protocol):

    def verify_and_update(
        self, plain_text: str, hashed_password: str
    ) -> Tuple[bool, Union[str, None]]: ... 

    def hash(self, password: str) -> str: ... 

    def generate(self) -> str: ... 

class PasswordHelper(PasswordHelperProtocol, PasswordService):

    def __init__(self, password_hash: Optional[PasswordHash] = None) -> None:
        if password_hash is None:
            self.password_hash = PasswordHash(
                (
                    Argon2Hasher(),
                    BcryptHasher()
                )
            )
        else:
            self.password_hash = password_hash

    def verify_and_update(self, plain_text:str, hashed_password:str) -> Tuple[bool, Union[str, None]]:
        print("veryfing the pass")
        return self.password_hash.verify_and_update(plain_text, hashed_password)

    
    def hash(self, password:str)-> str:
        return self.password_hash.hash(password)
    
    
    def generate(self) -> str:
        return secrets.token_urlsafe()
        

