from src.domain.entities.subject import Subject
from typing import List
from src.domain.enums.evaluation_type import EVALUATION_TYPE


class GradeViewmodel:
    value: float
    evaluationType: EVALUATION_TYPE
    weight: float

    def __init__(self, data:dict):
        self.value = data.get("value")
        self.evaluationType = data.get("evaluationType")
        self.weight = data.get("weight")

    def to_dict(self):
        return {
            "value": self.value,
            "evaluationType": self.evaluationType.value,
            "weight": self.weight
        }


class GetSubjectViewmodel:
    name: str
    code: str
    grades: List[GradeViewmodel]

    def __init__(self, data: Subject):
        att = data.dict()
        self.name = att["name"]
        self.code = att["code"]
        self.grades = [GradeViewmodel(grade) for grade in att.get("grades")] if att.get("grades") else []

    def to_dict(self):
        return {
            "name": self.name,
            "code": self.code,
            "grades": [grade.to_dict() for grade in self.grades]
        }
