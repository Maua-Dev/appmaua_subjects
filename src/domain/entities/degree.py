from typing import List
from pydantic import validator, BaseModel

from src.domain.errors.errors import EntityError


class Degree(BaseModel):
    name: str
    subjects: List[str]  # codeSubject
    duration: int
    codeDegree: str

    @validator('name')
    def name_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v

    @validator('duration')
    def duration_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('duration')
        return v

    @validator('subjects')
    def subjects_not_empty(cls, v: List[str]) -> List[str]:
        if len(v) == 0:
            raise EntityError('Subjects')
        return v

    @validator('codeDegree')
    def codeDegree_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('codeDegree')
        return v.upper()
