from enum import Enum
from typing import Dict, Union 
from pydantic import BaseModel

class ErrorModel(BaseModel):
    detail: Union[str, Dict[str, str]]


class ErrorCode(str, Enum):
    LOGIN_BAD_CREDENTIALS = "LOGIN_BAD_CREDENTIALS"
    LOGIN_USER_NOT_VERIFIED = "LOGIN_BAD_CREDENTIALS"
