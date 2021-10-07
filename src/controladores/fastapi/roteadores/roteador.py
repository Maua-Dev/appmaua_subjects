from fastapi import APIRouter

from .rotas.rotas_mss_info import RotaMssInfo
from .rotas.rotas_materias import RotaMaterias


class Roteador:

    def __call__(self, _ctrl):
        roteador = APIRouter()

        roteador.include_router(RotaMssInfo()())
        roteador.include_router(RotaMaterias()(_ctrl))

        return roteador

