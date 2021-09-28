import pytest

from src.repositorios.erros.erro_materia_nao_encontrada import ErroMateriaNaoEncontrada
from src.controladores.fastapi.c_get_materia_por_id import CGetMateriaPorIDFastapi
from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil

from devmaua.src.enum.tipo_email import TipoEmail
from devmaua.src.enum.tipo_telefone import TipoTelefone
from devmaua.src.enum.tipo_endereco import TipoEndereco
from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.tronco import Tronco
from devmaua.src.enum.nome_curso import NomeCurso
from devmaua.src.enum.tipo_sala import TipoSala
from devmaua.src.enum.campus import Campus
from devmaua.src.enum.semestralidade import Semestralidade
from devmaua.src.enum.tipo_disciplina import TipoDisciplina
from devmaua.src.enum.periodo import Periodo

from devmaua.src.models.aula import Aula
from devmaua.src.models.sala import Sala
from devmaua.src.models.professor import Professor
from devmaua.src.models.contato import Contato
from devmaua.src.models.email import Email
from devmaua.src.models.telefone import Telefone
from devmaua.src.models.endereco import Endereco
from devmaua.src.models.aluno import Aluno
from devmaua.src.models.ra import RA
from devmaua.src.models.disciplina import Disciplina


class TestCGetAllMateriasFastAPI():
    repo = MockRepositorioMateriasVolatil()
    ctrl = CGetMateriaPorIDFastapi(repo)
    id = 'ecm251'
    resposta: Disciplina = ctrl(id)

    assert type(resposta) is Disciplina
    assert resposta.codigo.value == "Linguagens de Programação I"
    assert resposta.tipo.value == 2  # GRADUAÇÃO
    assert resposta.semestralidade.value == 3
    assert resposta.profOrientador.nome == "Jorge Do Teste"
    assert resposta.aulas[0].local.bloco == "U"
    assert resposta.aulas[0].local.numeroDaSala == 22
    assert resposta.ofereceDp == True

    def erro_materia_nao_encontrada(self):
        id = 'esm251'
        with pytest.raises(ErroMateriaNaoEncontrada) as e:
            resposta = self.ctrl(id)
