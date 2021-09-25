from fastapi import HTTPException, status

from src.interfaces.IRepoMaterias import IRepoMaterias
from src.usecases.uc_get_materia_por_id_do_professor import UCGetMateriaPorIDProfessor
from src.repositorios.erros.erro_materia_nao_encontrada_pelo_id_professor import ErroMateriaNaoEncontradaPeloIDProfessor


class CGetMateriaPorIDProfessor:
    repo: IRepoMaterias

    def __init__(self, repo: IRepoMaterias):
        self.repo = repo

    def __call__(self, id: str):
        try:
            usecase = UCGetMateriaPorIDProfessor(self.repo)
            resposta = usecase(id)
        except ErroMateriaNaoEncontradaPeloIDProfessor as e:
            raise HTTPException(detail=str(e), status_code=status.HTTP_400_BAD_REQUEST)

        return resposta
