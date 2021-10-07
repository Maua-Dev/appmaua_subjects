from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_materias import RotasMaterias
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import FabricaControladorFastapi


class Roteador(APIRouter):

    def __init__(self, _ctrl: FabricaControladorFastapi):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasMaterias(_ctrl))
