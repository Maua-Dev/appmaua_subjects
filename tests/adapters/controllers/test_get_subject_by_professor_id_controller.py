import pytest
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import *


class Test_GetSubjectByProfessorIdController:

    @pytest.mark.asyncio
    async def test_get_subject_by_professor_id_controller(self):

        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': 1})
        answer = await getSubjectByProfessorIdController(req)

        assert type(answer.body) is list
        assert len(answer.body) == 3
        assert answer.status_code == 200

    @pytest.mark.asyncio
    async def test_get_subject_by_professor_id_controller_no_item_found(self):
        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': 3})
        answer = await getSubjectByProfessorIdController(req)

        assert type(answer) is NotFound
        assert answer.status_code == 404

    @pytest.mark.asyncio
    async def test_get_subject_by_professor_id_controller_error(self):
        getSubjectByProfessorIdController = GetSubjectByProfessorIdController(SubjectRepositoryMock())
        req = HttpRequest(query={'idProfessor': -1})
        answer = await getSubjectByProfessorIdController(req)

        assert type(answer) is BadRequest
        assert answer.status_code == 400
