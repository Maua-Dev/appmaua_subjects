from typing import List

from src.domain.entities.subject import Subject
from src.domain.enums.evaluation_type import EVALUATION_TYPE


class GradeViewModel:
    value: float
    evaluationType: EVALUATION_TYPE
    weight: float

    def __init__(self, data: dict):
        self.value = data.get("value")
        self.evaluationType = data.get("evaluationType")
        self.weight = data.get("weight")

    def to_dict(self):
        return {
            'value': self.value,
            'evaluationType': self.evaluationType.value,
            'weight': self.weight,
        }


class SubjectViewModel:
    name: str
    code: str
    grades: List[GradeViewModel]

    def __init__(self, data: dict):
        self.name = data.get("name")
        self.code = data.get("code")
        self.grades = [GradeViewModel(grade) for grade in data.get("grades")] if data.get("grades") else []

    def to_dict(self):
        return {
            'name': self.name,
            'code': self.code,
            'grades': [grade.to_dict() for grade in self.grades]
        }


class GetAllSubjectsViewmodel:
    subjects: List[SubjectViewModel] = []

    def __init__(self, data: List[Subject]):
        self.subjects = [SubjectViewModel(subject.dict()) for subject in data]

    def to_dict(self):
        return [subject.to_dict() for subject in self.subjects]
