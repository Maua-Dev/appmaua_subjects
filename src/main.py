import uvicorn
from typing import Union
from fastapi import HTTPException, status

from src.config.proj_config import ProjConfig
from src.controladores.fastapi.http.requisicoes import *
from src.controladores.fastapi.http.respostas import *
from src.init import Init

from devmaua.src.models.disciplina import Disciplina


def main():
    (_, _ctrl) = Init()()

    @_ctrl.app.get('/', response_model=ResRoot)
    async def root():
        req = ResRoot(
            deployment=ProjConfig.getDeployment(),
            controlador=ProjConfig.getFastapi()
        )

        print(req)
        return req

    @_ctrl.app.get('/materias', response_model=Union[Disciplina, list[Disciplina]])
    async def getMaterias(idmateria: str = None, idprof: str = None):
        if idmateria is None and idprof is None:
            return _ctrl.getAllMaterias()
        if idmateria is not None and idprof is None:
            return _ctrl.getMateriaPorID(idmateria)
        if idmateria is None and idprof is not None:
            return _ctrl.getMateriaPorIDProfessor(idprof)
        else:
            raise HTTPException(detail="Muitos argumentos foram passados", status_code=status.HTTP_400_BAD_REQUEST)

    return _, _ctrl


if __name__ == '__main__':
    (_, ctrl) = main()
    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
