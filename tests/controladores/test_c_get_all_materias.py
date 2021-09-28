from src.controladores.fastapi.c_get_all_materias import CGetAllMateriasFastapi
from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil


class TestCGetAllMateriasFastAPI():
    repo = MockRepositorioMateriasVolatil()
    ctrl = CGetAllMateriasFastapi(repo)
    resposta = ctrl()

    assert type(resposta) is list
