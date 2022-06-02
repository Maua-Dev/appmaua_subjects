from typing import List, Optional

from pydantic.main import BaseModel

from pydantic import validator

from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.period import PERIOD
from src.domain.enums.year import YEAR
from src.helpers.errors.domain_errors import EntityError


class Student(BaseModel):
    name: str
    ra: str
    email: str
    password: Optional[str] = None
    degreeCode: DegreeEnum
    subjects: List[Subject]
    academicYear: YEAR
    period: PERIOD
    photo: str

    @validator('name')
    def name_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v.title()

    #todo fazer os validators para os outros campos
    @validator('ra')
    def ra_is_not_empty(cls,v: str) -> str:
        if v != None and len(v) != 8:
            raise EntityError('RA')
        return v

    @validator('email')
    def email_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('Email')
        return v

    @validator('degreeCode')
    def degreeCode_is_not_empty(cls,v: DegreeEnum) -> DegreeEnum:
        if v is None:
            raise EntityError('DegreeCode')
        return v

    @validator('period')
    def period_is_not_empty(cls,v: PERIOD) -> PERIOD:
        if v is None:
            raise EntityError('Period')
        return v

    @validator('subjects')
    def subjects_is_not_empty(cls,v: List[Subject]) -> List[Subject]:
        if v is None:
            raise EntityError('Subjects')
        return v

    @validator('password')
    def password_is_not_empty(cls,v: str) -> str:
        if v is None:
            return v
        if len(v) == 0:
            raise EntityError('Password')
        return v

    @validator('academicYear')
    def academicYear_is_not_empty(cls,v: YEAR) -> YEAR:
        if v is None:
            raise EntityError('AcademicYear')
        return v

    @validator('photo')
    def photo_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v