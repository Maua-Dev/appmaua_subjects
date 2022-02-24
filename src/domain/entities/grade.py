from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError
from src.domain.enums.evaluation_type import EvaluationType


class Grade(BaseModel):
    value: float
    academicYear: int
    evaluationType: EvaluationType
    weight: float

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

    @validator('weight')
    def weight_is_valid(cls, v: float) -> float:
        if v <= 0:
            raise EntityError('weight')
        return v




