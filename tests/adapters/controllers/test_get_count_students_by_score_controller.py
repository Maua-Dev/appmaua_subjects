from src.adapters.controllers.get_count_students_by_score_controller import GetCountStudentsByScoreController
from src.adapters.viewmodels.bar_chart import GraphBar
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest
from src.domain.usecases.get_count_students_by_score_usecase import GetCountStudentsByScoreUsecase
import pytest
from typing import List


class Test_GetCountStudentsByScoreController:

    @pytest.mark.asyncio
    async def test_get_all_subjects_controller(self):

        getCountStudentsByScoreController = GetCountStudentsByScoreController(GetCountStudentsByScoreUsecase(SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 'ecm505',
                             'idEvaluationType': 1,
                             'academicYear': 2022})
        answer = await getCountStudentsByScoreController(req)

        assert type(answer.body.bars) is list
        assert len(answer.body.bars) == 23
        assert answer.status_code == 200
