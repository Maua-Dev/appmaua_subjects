from abc import ABC, abstractmethod
from typing import List, Tuple
from src.domain.entities.subject import Subject


class ISubjectRepository(ABC): #todo implementar os metodos

    @abstractmethod
    async def get_all_subjects(self) -> List[Subject]:
        pass
