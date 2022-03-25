from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError
from src.domain.enums.evaluation_type import EvaluationType


class Score(BaseModel):
    value: float
    academicYear: int
    evaluationType: EvaluationType
    weight: float

    @validator('academicYear')
    def academicYear_is_valid(cls, v: int) -> int:
        if v < 1960:
            raise EntityError('academicYear')
        return v

    @validator('value')
    def value_is_not_empty(cls, v: float) -> float:
        # -2 = NE
        # -1 = Zerado por Cola
        if v < -2 or (-2 < v < -1) or (-1 < v < 0) or v > 10:
            raise EntityError('Value')
        return v

    @validator('weight')
    def weight_is_valid(cls, v: float) -> float:
        if v <= 0:
            raise EntityError('weight')
        return v




