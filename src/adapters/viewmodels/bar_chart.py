from pydantic import BaseModel
from typing import List


class GraphBar(BaseModel):
    score: float
    studentCount: int

class BarChart(BaseModel):
    bars: List[GraphBar]
    courseStudentCount: int

