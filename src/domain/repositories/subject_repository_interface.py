from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC): #todo implementar os metodos

    @abstractmethod
    async def example(self, idStudent: int) -> List[Subject]:
        pass
