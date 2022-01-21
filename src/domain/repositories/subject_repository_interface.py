from abc import ABC, abstractmethod
from typing import List
from src.domain.entities.subject import Subject
class ISubjectRepository(ABC):
    @abstractmethod
    def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        pass