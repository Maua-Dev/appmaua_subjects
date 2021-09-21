from abc import ABC, abstractmethod


class IRepoMaterias(ABC):
    """ Interface de modificação de informações de um usuario """
    @abstractmethod
    def getAllMaterias(self) -> list:
        """ Retorna todas as matérias cadastradas """
        pass