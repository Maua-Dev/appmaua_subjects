from pydantic import ValidationError

from src.domain.entities.course import Course
from src.domain.entities.degree import Degree
from src.domain.entities.grade import Score
from src.domain.entities.student import Student
from src.domain.entities.subject import Subject


class SubjectDynamoDTO:


    def __init__(self, **kwargs) -> None:
        pass
        # Course
        # self.courseCode = kwargs.get("courseCode")
        # self.courseName = kwargs.get("courseName")
        #
        # # Degree
        # self.degreeName = kwargs.get("degreeName")
        # self.degreeDuration = kwargs.get("degreeDuration")
        # self.degreeCode = kwargs.get("degreeCode")
        # self.degreeSubjects = kwargs.get("degreeSubjects")
        #
        # # Score
        # self.scoreValue = kwargs.get("scoreValue")
        # self.scoreAcademicYear = kwargs.get("scoreAcademicYear")
        # self.scoreEvaluationType = kwargs.get("scoreEvaluationType")
        # self.scoreWeight = kwargs.get("scoreWeight")
        #
        # # Student
        # self.studentName = kwargs.get("studentName")
        # self.studentCode = kwargs.get("studentCode")
        # self.studentSubjects = kwargs.get("studentSubjects")
        # self.studentCodeDegree = kwargs.get("studentCodeDegree")
        #
        # # Subject
        # self.subjectCode = kwargs.get("subjectCode")
        # self.subjectName = kwargs.get("subjectName")

    def toEntity(self) -> dict:
        pass


    def toDynamo(self) -> dict:
        pass

