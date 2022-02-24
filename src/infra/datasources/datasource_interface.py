from abc import ABC, abstractmethod
from typing import List

from src.infra.dtos.Subject.subject_dto import SubjectDTO


class IDataSource(ABC):
    @abstractmethod
    def getSubjectsByStudent(self,idStudent: int) -> List[SubjectDTO]:
        pass

    @abstractmethod
    def getSubjectsByCode(self,codeSubject: str) -> SubjectDTO:
        pass

    @abstractmethod
    def getSubjectStudents(self, codeSubject: str) -> SubjectDTO:
        pass

    @abstractmethod
    def getAllSubjects(self) -> SubjectDTO:
        pass

    @abstractmethod
    def getSubjectByProfessorId(self, idProfessor: int) -> SubjectDTO:
        pass