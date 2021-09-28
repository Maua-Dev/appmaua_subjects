from src.interfaces.IRepoMaterias import IRepoMaterias

from devmaua.src.models.disciplina import Disciplina

from devmaua.src.enum.codigo_disciplina import CodigoDisciplina

class RepositorioMateriasVolatil(IRepoMaterias):

    materias: list[Disciplina]

    def __init__(self):
        self.materias = []

    def getAllMaterias(self):
        return self.materias

    def getMateriaPorID(self, id: str):
        materia = None
        for m in self.materias:
            if m.codigo == CodigoDisciplina[id.upper()]:
                materia = m
                break
        return materia

    def getMateriaPorIDProfessor(self, id: str):
        materias = []
        for m in self.materias:
            for p in m.professores:
                if p.ID.upper() == id.upper():
                    materias.append(m)
        return materias

