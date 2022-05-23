from pydantic import ValidationError

from src.domain.entities.course import Course
from src.domain.entities.degree import Degree
from src.domain.entities.score import Score
from src.domain.entities.student import Student
from src.domain.entities.subject import Subject


class SubjectDynamoDTO:
    entitiesData = {
        "Course": {
            "fields": [
                {
                    "dto": "courseCode",
                    "entity": "codeCourse"
                },
                {
                    "dto": "courseName",
                    "entity": "name"
                }
            ],
            "class": Course
        },
        "Degree": {
            "fields": [
                {
                    "dto": "degreeName",
                    "entity": "name"
                },
                {
                    "dto": "degreeDuration",
                    "entity": "duration"
                },
                {
                    "dto": "degreeCode",
                    "entity": "codeDegree"
                },
                {
                    "dto": "degreeSubjects",
                    "entity": "subjects",
                    "default": [""]
                }
            ],
            "class": Degree
        },
        "Score": {
            "fields": [
                {
                    "dto": "scoreValue",
                    "entity": "value"
                },
                {
                    "dto": "scoreAcademicYear",
                    "entity": "academicYear"
                },
                {
                    "dto": "scoreEvaluationType",
                    "entity": "evaluationType"
                },
                {
                    "dto": "scoreWeight",
                    "entity": "weight"
                }
            ],
            "class": Score
        },
        "Student": {
            "fields": [
                {
                    "dto": "studentName",
                    "entity": "name"
                },
                {
                    "dto": "studentCodeDegree",
                    "entity": "codeDegree"
                },
                {
                    "dto": "studentSubjects",
                    "entity": "subjects",
                    "default": ["NULL"]
                },
                {
                    "dto": "studentCode",
                    "entity": "ra"
                }

            ],
            "class": Student
        },
        "Subject": {
            "fields": [
                {
                    "dto": "subjectCode",
                    "entity": "codeSubject"
                },
                {
                    "dto": "subjectName",
                    "entity": "name"
                }
            ],
            "class": Subject
        }
    }

    def __init__(self, **kwargs) -> None:
        # Course
        self.courseCode = kwargs.get("courseCode")
        self.courseName = kwargs.get("courseName")

        # Degree
        self.degreeName = kwargs.get("degreeName")
        self.degreeDuration = kwargs.get("degreeDuration")
        self.degreeCode = kwargs.get("degreeCode")
        self.degreeSubjects = kwargs.get("degreeSubjects")

        # Score
        self.scoreValue = kwargs.get("scoreValue")
        self.scoreAcademicYear = kwargs.get("scoreAcademicYear")
        self.scoreEvaluationType = kwargs.get("scoreEvaluationType")
        self.scoreWeight = kwargs.get("scoreWeight")

        # Student
        self.studentName = kwargs.get("studentName")
        self.studentCode = kwargs.get("studentCode")
        self.studentSubjects = kwargs.get("studentSubjects")
        self.studentCodeDegree = kwargs.get("studentCodeDegree")

        # Subject
        self.subjectCode = kwargs.get("subjectCode")
        self.subjectName = kwargs.get("subjectName")

    def toEntity(self) -> dict:
        entities = {}
        for entityName in SubjectDynamoDTO.entitiesData.keys():
            try:
                entityData = SubjectDynamoDTO.entitiesData[entityName]
                entityDict = {}
                for field in entityData["fields"]:
                    entityDict[field["entity"]] = getattr(self, field.get("dto")) if hasattr(self, field.get("dto")) else field.get("default")

                entities[entityName] = entityData["class"].parse_obj(entityDict)

            except (AttributeError, ValidationError):
                entities[entityName] = None
        return entities


    def appendEntity(self, entity: any) -> None:
        for field in SubjectDynamoDTO.entitiesData[entity.__class__.__name__]["fields"]:
            setattr(self, field.get("dto"), getattr(entity, field.get("entity")))


    def toDynamoDTO(self) -> dict:
        item = {}
        item["subjectCode"] = self.subjectCode

        for entityName in SubjectDynamoDTO.entitiesData.keys():
            try:
                entityData = SubjectDynamoDTO.entitiesData[entityName]
                entityDict = {}
                for field in entityData["fields"]:
                    entityDict[field["dto"]] = getattr(self, field.get("entity")) if hasattr(self, field.get("entity")) else field.get("default")

                item[entityName] = entityDict

            except (AttributeError, ValidationError):
                item[entityName] = None
        return dto