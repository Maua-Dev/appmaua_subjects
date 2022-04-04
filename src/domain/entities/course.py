from pydantic import validator, BaseModel
from src.domain.errors.errors import EntityError


class Course(BaseModel):    
    codeCourse: str
    name: str

    @validator('codeCourse')
    def codeCourse_is_not_empty(cls,v: str) -> str:
        if len(v) == 0:
            raise EntityError('codeCourse')
        return v

    @validator('name')
    def name_is_not_empty(cls,v: str)-> str:
        if len(v) == 0:
            raise EntityError('Name')
        return v