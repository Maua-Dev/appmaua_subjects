from typing import Optional, List

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Student(BaseModel):
    name: str
    idDegree: int
    idSubjects: List[int]

    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0 or v is None:
            raise EntityError('Name')
        return v

    @validator('idDegree')
    def idDegree_is_not_empty(cls, v: int) -> int:
        if v == 0 or v is None:
            raise EntityError('idDegree')
        return v

    @validator('idSubjects')
    def idSubjects_is_not_empty(cls, v: List[int]) -> List[int]:
        if v == 0 or v is None:
            raise EntityError('idSubjects')
        return v
