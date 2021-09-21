from src.controladores.fastapi.http.respostas import ResPadrao
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
            resposta = ResPadrao(msg=str(usecase()))
        except ErroGetAllMaterias:
            resposta = ResPadrao(msg=str(ErroGetAllMaterias))

        return resposta