from typing import Optional, List

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Subject(BaseModel):    
    codeSubject: str
    name: str

    @validator('codeSubject')
    def codeSubject_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('CodeSubject')
        return v

    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v