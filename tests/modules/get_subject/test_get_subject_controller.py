import pytest
from src.helpers.http_models import HttpRequest
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_subject.get_subject_usecase import GetSubjectUsecase
from src.modules.get_subject.get_subject_controller import GetSubjectController

class Test_GetSubjectController:

    @pytest.mark.asyncio
    async def test_get_subject_controller(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectUsecase(repo)
        controller = GetSubjectController(usecase)

        req = HttpRequest(query_params={
            "ra": "19003315",
            "code": "ECM231"
        })
        res = await controller(req)

        assert res.status_code == 200
        assert res.body["name"] == "Engenharia de Software"

    @pytest.mark.asyncio
    async def test_get_subject_controller_no_items_found(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectUsecase(repo)
        controller = GetSubjectController(usecase)

        req = HttpRequest(query_params={
            "ra": "21010757",
            "code": "ECM231"
        })
        res = await controller(req)

        assert res.status_code == 404

