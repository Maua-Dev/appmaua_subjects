from typing import Union, List
from fastapi import APIRouter, Depends, HTTPException, status

from devmaua.src.models.disciplina import Disciplina


class RotaMaterias:
    def __call__(self, _ctrl):

        RoteadorMaterias = APIRouter(prefix="/materias",
                             responses={404: {"description": "Not found"}})

        @RoteadorMaterias.get('', response_model=Union[Disciplina, List[Disciplina]])
        async def getMaterias(idmateria: str = None, idprof: str = None):
            if idmateria is None and idprof is None:
                return _ctrl.getAllMaterias()
            if idmateria is not None and idprof is None:
                return _ctrl.getMateriaPorID(idmateria)
            if idmateria is None and idprof is not None:
                return _ctrl.getMateriaPorIDProfessor(idprof)
            else:
                raise HTTPException(detail="Muitos argumentos foram passados", status_code=status.HTTP_400_BAD_REQUEST)

        return RoteadorMaterias
