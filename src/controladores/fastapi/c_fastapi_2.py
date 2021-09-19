from src.controladores.fastapi.http.respostas import *
from src.interfaces.IRepo import IRepo
from src.usecases.uc_2 import UC2


class CFastapi2:
    repo: IRepo

    def __init__(self, repo: IRepo):
        self.repo = repo

    def __call__(self, arg):
        usecase = UC2(self.repo)
        return ResArg(
            arg=arg,
            msg=usecase(arg)
        )
