from src.adapters.controllers.get_score_statistics_controller import GetScoreStatisticsController
from src.adapters.viewmodels.bar_chart import GraphBar
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest
from src.domain.usecases.get_count_students_by_score_usecase import GetCountStudentsByScoreUsecase
from src.domain.usecases.get_count_students_by_course_and_year_usecase import GetCountStudentsByCourseAndYearUsecase
from src.domain.usecases.get_student_course_id_usecase import GetStudentCourseIdUsecase
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
import pytest
from typing import List


class Test_GetCountStudentsByScoreController:

    @pytest.mark.asyncio
    async def test_get_count_students_by_score_controller(self):
        getCountStudentsByScoreController = GetScoreStatisticsController(
            GetCountStudentsByScoreUsecase(SubjectRepositoryMock()),
            GetCountStudentsByCourseAndYearUsecase(SubjectRepositoryMock()),
            GetStudentCourseIdUsecase(SubjectRepositoryMock()),
            GetStudentCourseYearUsecase(SubjectRepositoryMock()))

        req = HttpRequest(query={'codeSubject': 'ecm505',
                                 'idEvaluationType': 1,
                                 'academicYear': 2022,
                                 'idStudent': 1})

        answer = await getCountStudentsByScoreController(req)

        assert type(answer.body.bars) is list
        assert len(answer.body.bars) == 23
        assert answer.status_code == 200
