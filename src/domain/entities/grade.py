from typing import List
from pydantic.class_validators import validator
from pydantic.main import BaseModel

from src.domain.errors.errors import EntityError

from src.domain.entities.subject import Subject

class Grade(BaseModel):
    value: float
    idGrade: int
    idStudent: int
    codeSubject: str

    @validator('idSubjects')
    def idSubjects_is_not_empty(cls, v: List[int]) -> List[int]:
        if len(v) == 0:
            raise EntityError('idSubjects')
        return v

    @validator('codeSubject')
    def codeSubject_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('CodeSubject')
        return v

    @validator('value')
    def value_is_not_empty(cls, v: float) -> float:
        if v < 0 or v > 10:
            raise EntityError('Value')
        return v

    @validator('idGrade')
    def idGrade_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('idGrade')
        return v



