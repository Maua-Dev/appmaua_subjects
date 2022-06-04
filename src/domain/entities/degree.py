import abc
from typing import List
from pydantic import BaseModel, validator

from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.helpers.errors.domain_errors import EntityError


class Degree(BaseModel, abc.ABC):
    name: str
    code: str
    subjects: List[Subject]
    coordinator: Professor

    # colocar os validators aqui - coordinator tem que ter name e email (@maua.br)
    # verificar se name e code existem em DegreeEnum

    @validator('name')
    def name_is_not_empty(cls, v:str) -> str:
        if len(v) == 0:
            raise EntityError('name')

    @validator('code')
    def code_is_not_empty(cls, v: str) -> str:
        if len(v) == 0:
            raise EntityError('code')
        return v

    @validator('coordinator')
    def coordinator_is_valid(cls, v: Professor) -> Professor:
        if v is None:
            raise EntityError('coordinator')
        return v

