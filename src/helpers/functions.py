from typing import List

from src.domain.entities.grade import Grade

#grade.value pode ser None, se nao tiver feito a prova ainda - isso conta no Current e nao conta no partial

def getCurrentGrade(grades: List[Grade]) -> float:
    current_grade = 0
    for grade in grades:
        if grade.value != None: #se for None, eu somaria à current_grade 0
            current_grade += grade.value * grade.weight

    return current_grade

def getPartialGrade(grades: List[Grade]) -> float:
    partial_grade = 0
    partial_weight = 0
    for grade in grades:
        if grade.value != None:
            partial_grade += grade.value * grade.weight
            partial_weight += grade.weight

    return partial_grade/partial_weight