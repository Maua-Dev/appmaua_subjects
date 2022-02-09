from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.domain.entities.subject import Subject
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest, NoContent, BadRequest


class Test_GetStudentSubjectsController():

    def test_get_student_subject_1(self):
        getStudentSubjectsController = GetStudentSubjectsController(getStudentSubjectsUsecase=GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'idStudent': 1})
        answer = getStudentSubjectsController(req)
        assert len(answer.body) == 2
        assert Subject(codeSubject='ECM501', name='Ciencia de dados') in answer.body
        assert Subject(codeSubject='ECM502', name='Devops') in answer.body
        assert answer.status_code == 200

    def test_get_student_subject_2(self):
        getStudentSubjectsController = GetStudentSubjectsController(getStudentSubjectsUsecase=GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'idStudent': 2})
        answer = getStudentSubjectsController(req)
        assert len(answer.body) == 3
        assert Subject(codeSubject='ECM501', name='Ciencia de dados') in answer.body
        assert Subject(codeSubject='ECM505', name='Banco de dados') in answer.body
        assert Subject(codeSubject='ECM503', name='Controladores') in answer.body
        assert answer.status_code == 200

    def test_get_student_subject_no_item_found(self):
        getStudentSubjectsController = GetStudentSubjectsController(getStudentSubjectsUsecase=GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'idStudent': 10})
        answer = getStudentSubjectsController(req)

        assert type(answer) is NoContent
        assert answer.status_code == 204

    def test_get_student_subject_invalid(self):
        getStudentSubjectsController = GetStudentSubjectsController(getStudentSubjectsUsecase=GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'idStudent': 0})
        answer = getStudentSubjectsController(req)

        assert type(answer) is BadRequest
        assert answer.status_code == 400
