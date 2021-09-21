from src.config.proj_config import ProjConfig
from src.config.erros.deployment import *
from src.config.enums.deployment import *
from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastapi


class Init:
    def __call__(
            self,
            tipo_repo: REPOSITORIO = ProjConfig.getDeployment()[KEY.TIPO_REPOSITORIO.value],
            tipo_ctrl: CONTROLADOR = ProjConfig.getDeployment()[KEY.TIPO_CONTROLADOR.value]
    ):
        # Instanciando tipo de REPOSITORIO
        if tipo_repo == REPOSITORIO.MOCK.value:
            repo = MockRepositorioMateriasVolatil()
        else:
            raise ErroDeployment1()

        # Instanciando tipo de CONTROLER
        if tipo_ctrl == CONTROLADOR.FASTAPI.value:
            ctrl = FabricaControladorFastapi(repo)
        else:
            raise ErroDeployment2()

        return repo, ctrl
