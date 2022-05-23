from typing import List

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Student(BaseModel):
    name: str
    codeDegree: str
    ra: str
    subjects: List[str]

    @validator('name')
    def name_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    @validator('codeDegree')
    def codeDegree_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('codeDegree')
        return v.upper()

    @validator('subjects')
    def subjects_is_valid(cls, v: List[str]) -> List[str]:
        for i in v:
            i = i.upper()
            if len(i) == 0:
                raise EntityError('subjects')
        return v

    @validator('ra')
    def ra_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('ra')
        return v
