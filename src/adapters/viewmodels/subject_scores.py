from pydantic import BaseModel
from typing import List, Optional

class SubjectScores(BaseModel):
    name: str
    finalScore: float
    isPartialScore: bool
    weights: dict
    testScores: dict
    workScores: dict
    subScores: dict