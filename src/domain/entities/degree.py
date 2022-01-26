from typing import List
from pydantic.class_validators import validator
from pydantic.main import BaseModel

from src.domain.errors.errors import EntityError

from src.domain.entities.subject import Subject


class Degree(BaseModel):
    name: str
    subjects: List[Subject]
    duration: int
    idCoordinator: int
    
    @validator('name')
    def name_is_not_empty(cls, v: str) -> str:
        if len(v) == 0 or v is None:
            raise EntityError('Name')
        return v
    
    @validator('duration')
    def duration_is_not_empty(cls, v: int) -> int:
        if v == 0 or v is None:
            raise EntityError('duration')
        return v

    @validator('subjects')
    def subjects_not_empty(cls, v: List[Subject]) -> List[Subject]:
        if len(v) == 0 or v is None:
            raise EntityError('Subjects')
        return v

    @validator('idCoordinator')
    def idcoordinator_is_not_empty(cls, v: int) -> int:
        if v == 0 or v is None:
            raise EntityError('idCoordinator')
        return v