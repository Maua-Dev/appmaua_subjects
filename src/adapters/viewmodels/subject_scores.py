from pydantic import BaseModel
from typing import List

class ScoreModel(BaseModel):
    idEvalType: int
    value: float

class SubjectScores(BaseModel):
    name: str
    finalScore: float
    isPartialScore: bool
    tests: List[ScoreModel]
    works: List[ScoreModel]
    subs: List[ScoreModel]