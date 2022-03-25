from pydantic import BaseModel
from typing import List, Optional

class AverageSubject(BaseModel):
    nome: str
    media: float
    isParcial: bool

class Course(BaseModel):
    curso: str
    cr: float
    materias: List[AverageSubject]