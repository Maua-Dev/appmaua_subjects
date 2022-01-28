from src.adapters.controllers.get_all_subjects_controller import GetStudentSubjectsController
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest

class Test_GetStudentSubjectsController():

    getStudentSubjectsController = GetStudentSubjectsController(SubjectRepositoryMock())
    req = HttpRequest(query=None)
    answer = getStudentSubjectsController(req)

    assert type(answer.body) is dict
    assert type(answer.body['subjects']) is list
    assert len(answer.body['subjects']) == 5
    assert answer.body['count'] == 5