from pydantic import BaseModel


class AverageViewModel(BaseModel):
    materia: str
    media: float

class AverageSubjectsViewModel(BaseModel):
    nomeGraduacao: str
    ano: int
    medias: list[AverageViewModel]
