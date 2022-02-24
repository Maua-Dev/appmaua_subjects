from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError
from ..enums.evaluation_type import EvaluationType


class Grade(BaseModel):
    value: float
    idGrade: int
    academicYear: int
    evaluationType: EvaluationType

    @validator('academicYear')
    def acdemicYear_is_valid(cls, v: int) -> int:
        if v < 1960:
            raise EntityError('academicYear')
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



