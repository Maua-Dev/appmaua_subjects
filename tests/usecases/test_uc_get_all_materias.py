import pytest

from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil

from src.usecases.uc_get_all_materias import UCGetAllMaterias

from src.repositorios.erros.erro_get_all_materias import ErroGetAllMaterias

from devmaua.src.models.disciplina import Disciplina

from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.semestralidade import Semestralidade
from devmaua.src.enum.tipo_disciplina import TipoDisciplina


class TestGetAllMaterias:

    def test_get_all_materias(self):
        repo = MockRepositorioMateriasVolatil()
        uc = UCGetAllMaterias(repo)
        materias = uc()

        assert len(materias) == 3

        email = repo.mockEmail()
        end = repo.mockEndereco()
        tel = repo.mockTelefone()
        contato = repo.mockContato(email, tel, end)
        professor = repo.mockProfessor(contato)
        ra = repo.mockRA()
        aluno = repo.mockAluno(contato, ra)
        sala = repo.mockSala()
        aula = repo.mockAula(sala, professor)

        assert Disciplina(codigo=CodigoDisciplina.ECM251,
                                           tipo=TipoDisciplina.PAE,
                                           semestralidade=Semestralidade.SEGUNDO_SEMESTRE,
                                           profOrientador=professor,
                                           professores=[professor],
                                           alunosMatriculados=[aluno],
                                           aulas=[aula],
                                           ofereceDp=True) in materias

        assert Disciplina(codigo=CodigoDisciplina.ECM251,
                                           tipo=TipoDisciplina.POS_GRADUACAO,
                                           semestralidade=Semestralidade.PRIMEIRO_SEMESTRE,
                                           profOrientador=professor,
                                           professores=[professor],
                                           alunosMatriculados=[aluno],
                                           aulas=[aula],
                                           ofereceDp=True) in materias

        assert Disciplina(codigo=CodigoDisciplina.ECM251,
                                tipo=TipoDisciplina.GRADUACAO,
                                semestralidade=Semestralidade.ANUAL,
                                profOrientador=professor,
                                professores=[professor],
                                alunosMatriculados=[aluno],
                                aulas=[aula],
                                ofereceDp=True) in materias