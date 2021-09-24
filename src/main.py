import uvicorn

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

    @_ctrl.app.get('/materias/', response_model=list[Disciplina])
    async def getAllMaterias():
        return _ctrl.getAllMaterias()

    @_ctrl.app.get('/materias/{id}', response_model=Disciplina)
    async def getMateriaPorID(id: str):
        return _ctrl.getMateriaPorID(id)

    return _, _ctrl


if __name__ == '__main__':
    (_, ctrl) = main()
    uvicorn.run(ctrl.app, host=ctrl.host, port=ctrl.porta)
