from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.domain.entities.subject import Subject
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest, NoContent


class Test_GetStudentSubjectsController():

    def test_get_student_subject_1(self):
        getStudentSubjectsController = GetStudentSubjectsController(SubjectRepositoryMock())
        req = HttpRequest(query={'idStudent': 1})
        answer = getStudentSubjectsController(req)

        assert type(answer.body) is dict
        assert type(answer.body['subjects']) is list
        assert len(answer.body['subjects']) == 2
        assert answer.body['count'] == 2
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in answer.body['subjects']
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in answer.body['subjects']
        assert answer.status_code == 200

    def test_get_student_subject_2(self):
        getStudentSubjectsController = GetStudentSubjectsController(SubjectRepositoryMock())
        req = HttpRequest(query={'idStudent': 2})
        answer = getStudentSubjectsController(req)

        assert type(answer.body) is dict
        assert type(answer.body['subjects']) is list
        assert len(answer.body['subjects']) == 3
        assert answer.body['count'] == 3
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in answer.body['subjects']
        assert Subject(id=5, codeSubject='ECM505', name='Banco de dados') in answer.body['subjects']
        assert Subject(id=6, codeSubject='ECM503', name='Controladores') in answer.body['subjects']
        assert answer.status_code == 200

    def test_get_student_subject_no_item_found(self):
        getStudentSubjectsController = GetStudentSubjectsController(SubjectRepositoryMock())
        req = HttpRequest(query={'idStudent': 0})
        answer = getStudentSubjectsController(req)

        assert type(answer) is NoContent
        assert answer.status_code == 204
