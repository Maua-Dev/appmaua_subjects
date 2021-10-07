from fastapi import APIRouter

from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.respostas import *


class RotaMssInfo:

    def __call__(self):

        RoteadorMssInfo = APIRouter(prefix="",
                             responses={404: {"description": "Not found"}})

        @RoteadorMssInfo.get("/", response_model=ResRoot)
        async def root():
            req = ResRoot(
                deployment=ProjConfig.getDeployment(),
                controlador=ProjConfig.getFastapi())

            print(req)
            return req

        return RoteadorMssInfo
