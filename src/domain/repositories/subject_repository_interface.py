from abc import ABC, abstractmethod
from typing import List
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
    async def getNumStudentsByScore(self, gradeValue: float, codeSubject:str, evaluationType: int,
                                     academicYear: int) -> int:
        pass

