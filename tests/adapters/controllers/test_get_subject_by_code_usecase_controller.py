from src.adapters.controllers.get_subject_by_code_usecase_controller import GetSubjectByCodeController
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest
from src.domain.entities.subject import Subject

class Test_GetAllSubjectsController:

    def test_get_all_subjects_controller(self):

        getSubjectByCodeController = GetSubjectByCodeController(SubjectRepositoryMock())
        req = HttpRequest(query={'codeSubject': 'ecm505'})
        answer = getSubjectByCodeController(req)

        assert type(answer.body) is dict
        assert type(answer.body['subject']) is Subject
        assert answer.body['count'] == 1
        assert answer.status_code == 200
