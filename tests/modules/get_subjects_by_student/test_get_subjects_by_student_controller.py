import pytest

from src.helpers.http_models import HttpRequest
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_subjects_by_student.get_subjects_by_student_controller import GetSubjectsByStudentController
from src.modules.get_subjects_by_student.get_subjects_by_student_usecase import GetSubjectsByStudentUsecase


class Test_GetSubjectsByStudentController:

    @pytest.mark.asyncio
    async def test_get_subjects_by_student_controller(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectsByStudentUsecase(repo)
        controller = GetSubjectsByStudentController(usecase)

        subject1 = repo.subjects[0]
        subject2 = repo.subjects[1]

        req = HttpRequest(query_params={"ra":"19003315"})

        res = await controller(req)

        assert res.status_code == 200
        assert len(res.body) == 2
        for subject_dict in res.body:
            assert subject_dict["code"] in [subject1.code, subject2.code]

        @pytest.mark.asyncio
        async def test_get_subjects_by_student_controller_no_items_found(self):
            repo = SubjectRepositoryMock()
            usecase = GetSubjectsByStudentUsecase(repo)
            controller = GetSubjectsByStudentController(usecase)

            req = HttpRequest(query_params={
                "ra": "21010757"
            })
            res = await controller(req)

            assert res.status_code == 404

        @pytest.mark.asyncio
        async def test_get_subjects_by_student_controller_bad_request(self):
            repo = SubjectRepositoryMock()
            usecase = GetSubjectsByStudentUsecase(repo)
            controller = GetSubjectsByStudentController(usecase)

            req = HttpRequest(query_params={})
            res = await controller(req)

            assert res.status_code == 400

