from fastapi import APIRouter

from .rotas.rotas_mss_info import RotasMssInfo
from .rotas.rotas_materias import RotasMaterias


class Roteador(APIRouter):

    def __init__(self, _ctrl):

        super().__init__()

        self.include_router(RotasMssInfo())
        self.include_router(RotasMaterias(_ctrl))
