from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest

class Test_GetAllSubjectsController:

    def test_get_all_subjects_controller(self):

        getAllSubjectsController = GetAllSubjectsController(SubjectRepositoryMock())
        req = HttpRequest(query=None)
        answer = getAllSubjectsController(req)

        assert type(answer.body) is dict
        assert type(answer.body['subjects']) is list
        assert len(answer.body['subjects']) == 5
        assert answer.body['count'] == 5
        assert answer.status_code == 200
