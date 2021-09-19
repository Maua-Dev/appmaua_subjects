from abc import ABC, abstractmethod


class IRepo(ABC):
    @abstractmethod
    def metodoRepo1(self) -> object:
        pass

    @abstractmethod
    def metodoRepo2(self, arg: object) -> object:
        pass
