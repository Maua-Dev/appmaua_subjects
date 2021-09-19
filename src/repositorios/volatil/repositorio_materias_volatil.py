from src.interfaces.i_getters_materias import IGettersMaterias

from devmaua.src.models.disciplina import Disciplina

class RepositorioMateriasVolatil(IGettersMaterias):

    repositorio: list[Disciplina]

    def __init__(self):
        self.repositorio = []

    def getAllMaterias(self) -> list:
        return self.repositorio
