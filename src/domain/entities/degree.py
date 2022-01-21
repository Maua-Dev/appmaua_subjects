from typing import List
from pydantic.class_validators import validator
from pydantic.main import BaseModel


from src.domain.errors.errors import EntityError

class Degree(BaseModel):
    name: str
    # subjects: List[Subject]
    duration: int
    
    @validator('name')
    def name_is_not_empty(cls,v):
        if len(v) == 0:
            raise EntityError('Name')
        return v
    
    @validator('duration')
    def duration_is_not_empty(cls,v):
        if v == 0:
            raise EntityError('duration')
        return v