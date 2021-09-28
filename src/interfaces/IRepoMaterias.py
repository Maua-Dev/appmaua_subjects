from abc import ABC, abstractmethod
from typing import List
from devmaua.src.models.disciplina import Disciplina


class IRepoMaterias(ABC):
    """ Interface de modificação de informações de um usuario """
    @abstractmethod
    def getAllMaterias(self) -> List[Disciplina]:
        """ Retorna todas as matérias cadastradas """
        pass

    @abstractmethod
    def getMateriaPorID(self, id: str) -> Disciplina:
        """ Retorna uma matéria (ou não) dado um id """
        pass

    @abstractmethod
    def getMateriaPorIDProfessor(self, id: str) -> List[Disciplina]:
        """ Retorna uma lista com todas as matérias ministradas por um professor """
        pass