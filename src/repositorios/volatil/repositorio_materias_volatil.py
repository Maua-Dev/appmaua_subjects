from src.interfaces.IRepoMaterias import IRepoMaterias

from devmaua.src.models.disciplina import Disciplina

from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

class RepositorioMateriasVolatil(IRepoMaterias):

    materias: list[Disciplina]

    def __init__(self):
        self.materias = []

    def getAllMaterias(self) -> list:
        return self.materias

    def getMateriaPorID(self, id: str) -> object:
        materia = None
        for m in self.materias:
            if m.codigo == CodigoDisciplina[id]:
                materia = m
                break
        return materia

    def getMateriaPorIDProfessor(self, id: str) -> list:
        materias = []
        for m in self.materias:
            for p in m.professores:
                if p.ID == id:
                    materias.append(m)
        return materias

