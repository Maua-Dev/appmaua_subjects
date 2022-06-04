from typing import List
import os
from boto3 import resource
import boto3

from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class SubjectRepositoryDynamo(ISubjectRepository):

    def __init__(self):
        s = boto3.Session(
            aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
            aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
        self.dynamo = s.resource('dynamodb', endpoint_url=os.environ.get('AWS_ENDPOINT_URL'))
        self.table = self.dynamo.Table(os.environ['DYNAMO_TABLE_NAME'])







    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        pass

    async def getSubjectStudents(self, codeSubject: str) -> tuple:
        pass

    async def getAllSubjects(self) -> tuple:
        pass

    async def getSubjectByCode(self, codeSubject: str) -> Subject:
        pass

    async def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        pass

    async def getCountStudentsByScore(self, gradeValue: float, codeSubject: str, idEvaluationType: int,
                                      academicYear: int, courseId: int, courseYear: int) -> int:
        pass

    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> float:
        pass

    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:
        pass

    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:
        pass

    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> List[int]:
        pass

    async def getCountStudentsByCourse(self, idCourse: int, courseYear: int, academicYear: int) -> int:
        pass

    async def getStudentCourseId(self, idStudent: int, academicYear: int) -> int:
        pass

    async def getStudentCourseYear(self, idStudent: int, academicYear: int) -> int:
        pass

    async def getCourseName(self, idCourse: int) -> str:
        pass

    async def getCourseNameByStudentId(self, idStudent: int) -> str:
        pass

    async def getSubjectNameById(self, idSubject: int) -> str:
        pass

    async def getSubjectCodeById(self, idSubject: int) -> str:
        pass