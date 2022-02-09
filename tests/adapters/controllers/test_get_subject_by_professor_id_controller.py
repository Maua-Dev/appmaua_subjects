from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest, NoContent, BadRequest


class Test_GetSubjectByProfessorIdController:

    def test_get_subject_by_professor_id_controller(self):

        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': 1})
        answer = getSubjectByProfessorIdController(req)

        assert type(answer.body) is list
        assert len(answer.body) == 3
        assert answer.status_code == 200

    def test_get_subject_by_professor_id_controller_no_item_found_id_3(self):
        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': 3})
        answer = getSubjectByProfessorIdController(req)

        assert type(answer) is NoContent
        assert answer.status_code == 204

    def test_get_subject_by_professor_id_controller_error(self):
        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': "1"})
        answer = getSubjectByProfessorIdController(req)

        assert type(answer) is BadRequest
        assert answer.status_code == 400
