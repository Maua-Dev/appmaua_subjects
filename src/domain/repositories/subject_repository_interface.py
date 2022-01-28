from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC):

    @abstractmethod
    def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        pass

    @abstractmethod
    def getSubjectStudents(self, codeSubject: str) -> List[int]:
        pass

    @abstractmethod
    def getAllSubjects(self) -> List[Subject]:
        pass

    @abstractmethod
    def getSubjectById(self, codeSubject: str) -> Subject:
        pass

    @abstractmethod
    def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:
        pass