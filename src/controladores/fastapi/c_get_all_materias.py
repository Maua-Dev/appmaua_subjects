from fastapi import Response, status

from src.interfaces.IRepoMaterias import IRepoMaterias
from src.usecases.uc_get_all_materias import UCGetAllMaterias
from src.repositorios.erros.erro_get_all_materias import ErroGetAllMaterias


class CGetAllMateriasFastapi:
    repo: IRepoMaterias

    def __init__(self, repo: IRepoMaterias):
        self.repo = repo

    def __call__(self):
        try:
            usecase = UCGetAllMaterias(self.repo)
            resposta = usecase()
        except ErroGetAllMaterias as e:
            resposta = Response(content=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        return resposta