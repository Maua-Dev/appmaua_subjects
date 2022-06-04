from typing import Optional

from pydantic import validator, BaseModel

from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.helpers.errors.domain_errors import EntityError


class Grade(BaseModel):
    value: Optional[float]  # None significa que ainda não foi avaliado
    evaluationType: EVALUATION_TYPE
    weight: float

    @validator('value')
    def value_is_not_empty(cls, v: float) -> float:
        # -2 = NE
        # -1 = Zerado por Cola
        if v is None:
            return v
        if not (((0 <= v <= 10) or v == -2 or v == -1)):
            raise EntityError('Value')
        return v

    @validator('weight')
    def weight_is_valid(cls, v: float) -> float:
        if v <= 0:
            raise EntityError('weight')
        return v
