from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC):

    @abstractmethod
    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:    
        pass
    @abstractmethod
    async def getSubjectStudents(self, codeSubject: str) -> tuple:
        pass

    @abstractmethod
    async def getAllSubjects(self) -> tuple:
        pass

    @abstractmethod
    async def getSubjectByCode(self, codeSubject: str) -> Subject:
        pass

    @abstractmethod
    async def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        pass

    @abstractmethod
    async def getCountStudentsByScore(self, gradeValue: float, codeSubject:str, idEvaluationType: int,
                                     academicYear: int) -> int:
        pass

    @abstractmethod
    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> float:
        pass

    @abstractmethod
    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:
        pass

    @abstractmethod
    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:
        pass

    @abstractmethod
    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> List[int]:
        pass


    @abstractmethod
    async def getCountStudentsByCourse(self, idCourse: int, courseYear: int) -> int:
        pass

    @abstractmethod
    async def getStudentCourseId(self, idStudent: int) -> int:
        pass