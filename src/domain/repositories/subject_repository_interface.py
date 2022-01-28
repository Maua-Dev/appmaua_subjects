from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC):

    @abstractmethod
    def getStudentSubjects(self, idStudent: int) -> tuple:
        pass
    @abstractmethod
    def getSubjectStudents(self, codeSubject: str) -> tuple:
        pass

    @abstractmethod
    def getAllSubjects(self) -> tuple:
        pass

    @abstractmethod
    def getSubjectByCode(self, codeSubject: str) -> tuple:
        pass

    @abstractmethod
    def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        pass