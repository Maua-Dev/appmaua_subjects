from src.interfaces.IRepo import IRepo
from src.repositorios.erros.erro_repo import ErroRepo
from src.models.erros.erro_dominio import ErroDominio


class UC1:
    repo: IRepo

    def __init__(self, repo: IRepo):
        self.repo = repo

    def __call__(self):
        if ():
            raise ErroDominio()
        elif ():
            raise ErroDominio()
        else:
            try:
                return self.repo.metodoRepo1()
            except ErroRepo as erro:
                raise erro
