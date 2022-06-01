import pytest

from src.helpers.http_models import HttpRequest
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_all_subjects.get_all_subjects_controller import GetAllSubjectsController
from src.modules.get_all_subjects.get_all_subjects_usecase import GetAllSubjectsUsecase


class Test_GetAllSubjectsController:

    @pytest.mark.asyncio
    async def test_get_all_subjects_controller(self):
        repo = SubjectRepositoryMock()
        expeted1 = repo.subjects[0]
        expeted2 = repo.subjects[1]

        usecase = GetAllSubjectsUsecase(repo)
        controller = GetAllSubjectsController(usecase)

        req = HttpRequest()

        res = await controller(req)

        assert res.status_code == 200
        assert len(res.body) == 2
        for i in res.body:
            assert i['code'] in [expeted1.code, expeted2.code]
            assert i['name'] in [expeted1.name, expeted2.name]



    @pytest.mark.asyncio
    async def test_get_all_subjects_controller_no_subjects(self):
        repo = SubjectRepositoryMock()

        repo.subjects = []

        usecase = GetAllSubjectsUsecase(repo)
        controller = GetAllSubjectsController(usecase)

        req = HttpRequest()

        res = await controller(req)

        assert res.status_code == 404
