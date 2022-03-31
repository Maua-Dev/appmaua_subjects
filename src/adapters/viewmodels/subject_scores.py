from pydantic import BaseModel
from typing import List, Optional

class ScoreModel(BaseModel):
    idEvalType: int
    evalName: str
    value: Optional[float]

class WeightModel(BaseModel):
    idEvalType: int
    evalName: str
    weight: Optional[int]

class SubjectScores(BaseModel):
    name: str
    finalScore: float
    isPartialScore: bool
    weights: List[WeightModel]
    testScores: List[ScoreModel]
    workScores: List[ScoreModel]
    subScores: List[ScoreModel]