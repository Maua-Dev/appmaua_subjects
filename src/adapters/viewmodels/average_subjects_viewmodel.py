from pydantic import BaseModel
from typing import List


class AverageViewModel(BaseModel):
    materia: str
    media: float
    isPartialScore:bool


class AverageSubjectsViewModel(BaseModel):
    nomeGraduacao: str
    ano: int
    medias: List[AverageViewModel]
