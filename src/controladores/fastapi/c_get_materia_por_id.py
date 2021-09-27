from fastapi import HTTPException, status

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
            resposta = usecase(id)
        except ErroMateriaNaoEncontrada as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            raise HTTPException(detail="Erro inesperado ao tentar encontrar matéria pelo ID: " + str(e),
                                     status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return resposta
