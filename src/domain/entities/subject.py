from typing import Optional, List

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Subject(BaseModel):    
    codeSubject: str
    name: str
    idProfessor: int
    idStudents: List[int]

    @validator('codeSubject')
    def codeSubject_is_not_empty(cls,v: str) -> str:
        if len(v) == 0 or v is None:
            raise EntityError('CodeSubject')
        return v

    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0 or v is None:
            raise EntityError('Name')
        return v

    @validator('idProfessor')
    def idprofessor_is_not_empty(cls, v: int) -> int:
        if v == 0 or v is None:
            raise EntityError('idProfessor')
        return v

    @validator('idStudents')
    def idstudents_is_not_null(cls, v: List[int]) -> List[int]:
        if v is None:
            raise EntityError('idStudents')
        return v