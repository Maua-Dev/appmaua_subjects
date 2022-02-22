from typing import Optional, List

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Subject(BaseModel):    
    codeSubject: str
    name: str
    idGrades: List[int]

    @validator('idGrades')
    def idGrades_is_not_empty(cls, v: List[int]) -> List[int]:
        if len(v) == 0:
            raise EntityError('idSubjects')
        return v

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