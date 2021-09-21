from src.controladores.fastapi.http.respostas import ResPadrao
from src.interfaces.IRepoMaterias import IRepoMaterias
from src.usecases.uc_get_materia_por_id import UCGetMateriaPorID
from src.repositorios.erros.erro_materia_nao_encontrada import ErroMateriaNaoEncontrada


class CGetMateriaPorIDFastapi:
    repo: IRepoMaterias

    def __init__(self, repo: IRepoMaterias):
        self.repo = repo

    def __call__(self, id: str):
        try:
            usecase = UCGetMateriaPorID(self.repo)
            resposta = ResPadrao(msg=str(usecase(id)))
        except ErroMateriaNaoEncontrada:
            resposta = ResPadrao(msg=str(ErroMateriaNaoEncontrada))
        except Exception as e:
            resposta = ResPadrao(msg="Erro inesperado ao tentar encontrar matéria pelo ID: " + str(e))

        return resposta
