from src.controladores.fastapi.c_get_materia_por_id import CGetMateriaPorIDFastapi
from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil
from src.controladores.fastapi.http.respostas import ResPadrao

class TestCGetAllMateriasFastAPI():
    repo = MockRepositorioMateriasVolatil()
    ctrl = CGetMateriaPorIDFastapi(repo)
    id = 'ecm251'
    resposta = ctrl(id)

    assert type(resposta) is ResPadrao
