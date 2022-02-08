from pydantic import BaseModel

from src.domain.entities.subject import Subject


class Grade(BaseModel):
    subject: Subject
    grade: float
    weight: int