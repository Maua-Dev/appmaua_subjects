from src.interfaces.IRepoMaterias import IRepoMaterias

from devmaua.src.models.disciplina import Disciplina

class RepositorioMateriasVolatil(IRepoMaterias):

    materias: list[Disciplina]

    def __init__(self):
        self.materias = []

    def getAllMaterias(self) -> list:
        return self.materias
