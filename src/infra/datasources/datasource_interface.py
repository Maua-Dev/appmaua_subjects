from abc import ABC, abstractmethod
from typing import List

from src.infra.dtos.Subject.subject_dto import SubjectDTO


class IDataSource(ABC):
    @abstractmethod
    def getSubjectsByStudent(self,idStudent: int) -> List[SubjectDTO]:
        pass