from pydantic import BaseModel
from typing import List, Optional

class ScoreModel(BaseModel):
    idEvalType: int
    value: Optional[float]

class SubjectScores(BaseModel):
    name: str
    finalScore: float
    isPartialScore: bool
    tests: List[ScoreModel]
    works: List[ScoreModel]
    subs: List[ScoreModel]