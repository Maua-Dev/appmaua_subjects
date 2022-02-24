from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError


class Grade(BaseModel):
    value: float
    idGrade: int
    idStudent: int
    codeSubject: str
    academicYear: int

    @validator('academicYear')
    def acdemicYear_is_valid(cls, v: int) -> int:
        if v < 1960:
            raise EntityError('academicYear')
        return v

    @validator('idStudent')
    def idStudent_is_not_empty(cls, v: int) -> int:
        if v == 0:
            raise EntityError('idStudent')
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



