from abc import ABC, abstractmethod
from typing import List

from src.infra.dtos.Subject import *


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
                                     academicYear: int) -> StudentScoresDTO:
        pass

    @abstractmethod
    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> StudentScoresDTO:
        pass

    @abstractmethod
    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalDataDTO:
        pass

    @abstractmethod
    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalWeightDTO:
        pass

    @abstractmethod
    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalWeightDTO:
        pass