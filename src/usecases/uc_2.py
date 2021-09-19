from src.interfaces.IRepo import IRepo
from src.repositorios.erros.erro_repo import ErroRepo
from src.models.erros.erro_dominio import ErroDominio


class UC2:
    repo: IRepo

    def __init__(self, repo: IRepo):
        self.repo = repo

    def __call__(self, arg):
        if ():
            raise ErroDominio()
        elif ():
            raise ErroDominio()
        else:
            try:
                return self.repo.metodoRepo2(arg)
            except ErroRepo as erro:
                raise erro
