from pydantic import validator

from src.helpers.errors.domain_errors import EntityError
from pydantic.main import BaseModel


class Professor(BaseModel):
    name: str
    email: str
    phoneNumber: str

    @validator('name')
    def name_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    @validator('email')
    def email_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('Email')
        return v

    @validator('phoneNumber')
    def phoneNumber_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('phoneNumber')
        return v