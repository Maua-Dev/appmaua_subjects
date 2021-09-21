from src.interfaces.IRepoMaterias import IRepoMaterias

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

class MockRepositorioMateriasVolatil(IRepoMaterias):

    repositorio: list[Disciplina]

    def __init__(self):
        email = self.mockEmail()
        end = self.mockEndereco()
        tel = self.mockTelefone()
        contato = self.mockContato(email, tel, end)
        professor = self.mockProfessor(contato)
        ra = self.mockRA()
        aluno = self.mockAluno(contato, ra)
        sala = self.mockSala()
        aula = self.mockAula(sala, professor)

        self.repositorio = []
        self.repositorio.append(Disciplina(codigo=CodigoDisciplina.ECM251,
                                tipo=TipoDisciplina.GRADUACAO,
                                semestralidade=Semestralidade.ANUAL,
                                profOrientador=professor,
                                professores=[professor],
                                alunosMatriculados=[aluno],
                                aulas=[aula],
                                ofereceDp=True))
        self.repositorio.append(Disciplina(codigo=CodigoDisciplina.ECM251,
                                           tipo=TipoDisciplina.POS_GRADUACAO,
                                           semestralidade=Semestralidade.PRIMEIRO_SEMESTRE,
                                           profOrientador=professor,
                                           professores=[professor],
                                           alunosMatriculados=[aluno],
                                           aulas=[aula],
                                           ofereceDp=True))
        self.repositorio.append(Disciplina(codigo=CodigoDisciplina.ECM251,
                                           tipo=TipoDisciplina.PAE,
                                           semestralidade=Semestralidade.SEGUNDO_SEMESTRE,
                                           profOrientador=professor,
                                           professores=[professor],
                                           alunosMatriculados=[aluno],
                                           aulas=[aula],
                                           ofereceDp=True))

    def getAllMaterias(self) -> list:
        return self.repositorio

    def addMateria(self, materia: Disciplina) -> None:
        self.repositorio.append(materia)

    def removerMateria(self, materia: Disciplina) -> None:
        if materia in self.repositorio:
            self.repositorio.remove(materia)

    def mockEmail(self):
        return Email(email='teste@teste.com',
              tipo=TipoEmail.PRIVADO,
              prioridade=1)

    def mockEndereco(self):
        return Endereco(logradouro='rua de tal',
                       numero=20,
                       cep='00000-000',
                       tipo=TipoEndereco.RESIDENCIAL)

    def mockTelefone(self):
        return Telefone(tipo=TipoTelefone.PRIVADO,
                       numero='99999-9999',
                       ddd=11,
                       prioridade=3)

    def mockContato(self, email: Email, tel: Telefone, end: Endereco):
        return Contato(emails=[email],
                          telefones=[tel],
                          enderecos=[end])

    def mockProfessor(self, contato: Contato):
        return Professor(nome='jorge do teste',
                              contato=contato,
                              nascimento='1999-02-23',
                              ID='0002',
                              troncos=[Tronco.ELETRICA],
                              cursos=[NomeCurso.ENGENHARIA_DA_COMPUTACAO],
                              disciplinas=[CodigoDisciplina.ECM251])

    def mockRA(self):
        return RA(ano='19',
                numero='02009',
                digito='0')

    def mockAluno(self, contato: Contato, ra: RA):
        return Aluno(nome='jorge do teste',
                      contato=contato,
                      nascimento='1999-02-23',
                      ra=ra,
                      curso=NomeCurso.ENGENHARIA_DA_COMPUTACAO,
                      serie=3,
                      disciplinas=[CodigoDisciplina.ECM251],
                      periodo=Periodo.DIURNO,
                      listaDPs=[],
                      hasDP=False)

    def mockSala(self):
        return Sala(bloco='U',
                    numeroDaSala=22,
                    tipo=[TipoSala.LABORATORIO],
                    campus=Campus.SCS)

    def mockAula(self, sala:Sala, professor: Professor):
        return Aula(disciplina=CodigoDisciplina.ECM251,
                    local=sala,
                    horario='2021-07-12 07:40:00',
                    duracao='01:40:00',
                    professor=professor)