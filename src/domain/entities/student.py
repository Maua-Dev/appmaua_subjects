from typing import Optional, List, Dict

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.errors.errors import EntityError


class Student(BaseModel):
    name: str
    idDegree: int
    idSubjects: List[int]
    idGradesBySubject: dict #Dict[int:int] ? /// idGrades is unique for each grade?

    @validator('idGradesBySubject')]
    def idGradesBySubject_is_not_empty(cls, v: dict) -> dict:
        if len(v) == 0:
            raise EntityError('idGradesBySubject')
        return v

    @validator('name')
    def name_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    @validator('idDegree')
    def idDegree_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('idDegree')
        return v

    @validator('idSubjects')
    def idSubjects_is_not_empty(cls, v: List[int]) -> List[int]:
        if len(v) == 0:
            raise EntityError('idSubjects')
        return v
