from src.controladores.fastapi.http.respostas import ResPadrao
from src.interfaces.IRepo import IRepo
from src.usecases.uc_1 import UC1


class CFastapi1:
    repo: IRepo

    def __init__(self, repo: IRepo):
        self.repo = repo

    def __call__(self):
        usecase = UC1(self.repo)
        return ResPadrao(msg=usecase())
