import abc
from typing import List
from pydantic import BaseModel

from src.domain.entities.subject import Subject


class Degree(BaseModel, abc.ABC):
    name: str
    code: str
    subjects: List[Subject]
    coordinator: dict

    # colocar os validators aqui - coordinator tem que ter name e email (@maua.br)
    # verificar se name e code existem em DegreeEnum
