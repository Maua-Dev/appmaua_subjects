from src.interfaces.IRepoMaterias import IRepoMaterias
from src.repositorios.erros.erro_materia_nao_encontrada import ErroMateriaNaoEncontrada


class UCGetMateriaPorID:
    repo: IRepoMaterias

    def __init__(self, repo: IRepoMaterias):
        self.repo = repo

    def __call__(self, id: str):
        try:
            materia = self.repo.getMateriaPorID(id.upper())
            if materia is None:
                raise ErroMateriaNaoEncontrada
        except KeyError:
            raise ErroMateriaNaoEncontrada

        return materia