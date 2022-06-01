from typing import List

from src.domain.entities.grade import Grade

#grade.value pode ser None, se nao tiver feito a prova ainda - isso conta no Current e nao conta no partial

def getCurrentGrade(grades: List[Grade]) -> float:

    pass

def getPartialGrade(grades: List[Grade]) -> float:
    pass