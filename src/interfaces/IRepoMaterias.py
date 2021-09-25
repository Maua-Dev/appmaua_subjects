from abc import ABC, abstractmethod


class IRepoMaterias(ABC):
    """ Interface de modificação de informações de um usuario """
    @abstractmethod
    def getAllMaterias(self) -> list:
        """ Retorna todas as matérias cadastradas """
        pass

    @abstractmethod
    def getMateriaPorID(self, id: str) -> object:
        """ Retorna uma matéria (ou não) dado um id """
        pass

    @abstractmethod
    def getMateriaPorIDProfessor(self, id: str) -> list:
        """ Retorna uma lista com todas as matérias ministradas por um professor """
        pass