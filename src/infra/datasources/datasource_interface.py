from abc import ABC, abstractmethod
from typing import List

from src.infra.dtos.Subject.subject_dto import SubjectDTO


class IDataSource(ABC):
    @abstractmethod
    async def getSubjectsByStudent(self,idStudent: int) -> List[SubjectDTO]:
        pass

    @abstractmethod
    async def getSubjectsByCode(self,codeSubject: str) -> SubjectDTO:
        pass

    @abstractmethod
    async def getSubjectStudents(self, codeSubject: str) -> SubjectDTO:
        pass

    @abstractmethod
    async def getAllSubjects(self) -> SubjectDTO:
        pass

    @abstractmethod
    async def getSubjectByProfessorId(self, idProfessor: int) -> SubjectDTO:
        pass

    @abstractmethod
    async def getCountStudentsByScore(self, gradeValue: float, codeSubject:str, idEvaluationType: int,
                                     academicYear: int) -> SubjectDTO:
        pass