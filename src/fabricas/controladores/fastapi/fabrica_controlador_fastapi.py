from fastapi import FastAPI

from src.config.proj_config import ProjConfig
from src.config.enums.fastapi import *
from src.controladores.fastapi.c_fastapi_1 import CFastapi1
from src.controladores.fastapi.c_fastapi_2 import CFastapi2
from src.interfaces.IRepo import IRepo


class FabricaControladorFastapi:
    repo: IRepo

    __config__: dict

    protocolo: str
    host: str
    porta: str
    root: str
    url: str

    app: FastAPI

    def __init__(self, repo: IRepo):
        self.repo = repo

        self.__config__ = ProjConfig.getFastapi()

        self.protocolo = self.__config__[KEY.PROTOCOLO.value]
        self.host = self.__config__[KEY.HOST.value]
        self.porta = self.__config__[KEY.PORTA.value]
        self.root = self.__config__[KEY.ROOT.value]
        self.url = f'{self.protocolo}://{self.host}:{self.porta}{self.root}'

        self.app = FastAPI()

    def metodoControlador1(self) -> object:
        return CFastapi1(self.repo)()

    def metodoControlador2(self, arg: object) -> object:
        return CFastapi2(self.repo)(arg)
