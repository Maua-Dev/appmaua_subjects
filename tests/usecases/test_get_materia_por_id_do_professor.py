import pytest

from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil

from src.usecases.uc_get_materia_por_id_do_professor import UCGetMateriaPorIDProfessor

from src.repositorios.erros.erro_materia_nao_encontrada_pelo_id_professor import ErroMateriaNaoEncontradaPeloIDProfessor

from devmaua.src.models.disciplina import Disciplina

from devmaua.src.enum.codigo_disciplina import CodigoDisciplina
from devmaua.src.enum.semestralidade import Semestralidade
from devmaua.src.enum.tipo_disciplina import TipoDisciplina


class TestGetMateriaPorIDProfessor:
    repo = MockRepositorioMateriasVolatil()
    uc = UCGetMateriaPorIDProfessor(repo)

    def test_get_materia_por_id_professor(self):
        id: str = '0002'
        materias = self.uc(id)

        email = self.repo.mockEmail()
        end = self.repo.mockEndereco()
        tel = self.repo.mockTelefone()
        contato = self.repo.mockContato(email, tel, end)
        professor = self.repo.mockProfessor(contato)
        ra = self.repo.mockRA()
        aluno = self.repo.mockAluno(contato, ra)
        sala = self.repo.mockSala()
        aula = self.repo.mockAula(sala, professor)

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

    def test_materia_inexistente(self):
        id: str = 'efb301'
        with pytest.raises(ErroMateriaNaoEncontradaPeloIDProfessor) as e:
            materia = self.uc(id)

