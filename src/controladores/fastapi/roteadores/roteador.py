from typing import Union, List
from fastapi import APIRouter, Depends, HTTPException, status

from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.respostas import *
from src.init import Init

from devmaua.src.models.disciplina import Disciplina

Roteador = APIRouter(prefix="",
                     dependencies=[Depends(Init)],
                     responses={404: {"description": "Not found"}})
(_, _ctrl) = Init()()


@Roteador.get("/", response_model=ResRoot)
async def root():
    req = ResRoot(
        deployment=ProjConfig.getDeployment(),
        controlador=ProjConfig.getFastapi())

    print(req)
    return req


@Roteador.get('/materias', response_model=Union[Disciplina, List[Disciplina]])
async def getMaterias(idmateria: str = None, idprof: str = None):
    if idmateria is None and idprof is None:
        return _ctrl.getAllMaterias()
    if idmateria is not None and idprof is None:
        return _ctrl.getMateriaPorID(idmateria)
    if idmateria is None and idprof is not None:
        return _ctrl.getMateriaPorIDProfessor(idprof)
    else:
        raise HTTPException(detail="Muitos argumentos foram passados", status_code=status.HTTP_400_BAD_REQUEST)
