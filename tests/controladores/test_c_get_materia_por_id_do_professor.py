import pytest

from src.repositorios.erros.erro_materia_nao_encontrada_pelo_id_professor import ErroMateriaNaoEncontradaPeloIDProfessor
from src.controladores.fastapi.c_get_materia_por_id_do_professor import CGetMateriaPorIDProfessor
from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil


class TestCGetAllMateriasFastAPI():
    repo = MockRepositorioMateriasVolatil()
    ctrl = CGetMateriaPorIDProfessor(repo)

    def test_get_materia_por_id_prof(self):
        id = '0002'
        resposta = self.ctrl(id)

        assert type(resposta) is list
        assert len(resposta) == 3

    def erro_materia_nao_encontrada(self):
        id = '0003'
        with pytest.raises(ErroMateriaNaoEncontradaPeloIDProfessor) as e:
            resposta = self.ctrl(id)