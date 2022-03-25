from src.adapters.controllers.get_student_subject_scores_controller import GetStudentSubjectScoreController
from src.adapters.viewmodels.subject_scores import *
from src.domain.usecases.get_final_score_usecase import GetFinalScoreUsecase
from src.domain.usecases.get_student_subject_score_usecase import GetStudentSubjectScoreUsecase
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import HttpRequest
from src.domain.usecases.get_subject_evaluation_quantity_usecase import GetSubjectEvaluationQuantityUsecase
import pytest


class Test_GetStudentSubjectScoreController:

    @pytest.mark.asyncio
    async def test_get_student_scores_controller_1(self):

        getStudentSubjectScoreController = GetStudentSubjectScoreController(
            getStudentSubjectScoreUsecase=GetStudentSubjectScoreUsecase(SubjectRepositoryMock()),
            getSubjectByCodeUsecase=GetSubjectByCodeUsecase(SubjectRepositoryMock()),
            getFinalScoreUsecase=GetFinalScoreUsecase(SubjectRepositoryMock()),
            getSubjectEvaluationQuantityUsecase=GetSubjectEvaluationQuantityUsecase(SubjectRepositoryMock()))

        req = HttpRequest(query={'codeSubject': 'ecm505',
                                 'idStudent': 1,
                                 'academicYear': 2022})
        answer = await getStudentSubjectScoreController(req)

        body: SubjectScores = answer.body

        assert type(body.tests) is list
        assert len(body.tests) == 2

        assert type(body.works) is list
        assert len(body.works) == 4

        assert type(body.subs) is list
        assert len(body.subs) == 1

        assert body.name == "Banco de dados"

        assert body.finalScore == 8.9

        assert body.isPartialScore is False

        assert answer.status_code == 200

    @pytest.mark.asyncio
    async def test_get_student_scores_controller_2(self):
        getStudentSubjectScoreController = GetStudentSubjectScoreController(
            getStudentSubjectScoreUsecase=GetStudentSubjectScoreUsecase(SubjectRepositoryMock()),
            getSubjectByCodeUsecase=GetSubjectByCodeUsecase(SubjectRepositoryMock()),
            getFinalScoreUsecase=GetFinalScoreUsecase(SubjectRepositoryMock()),
            getSubjectEvaluationQuantityUsecase=GetSubjectEvaluationQuantityUsecase(SubjectRepositoryMock()))

        req = HttpRequest(query={'codeSubject': 'ecm501',
                                 'idStudent': 1,
                                 'academicYear': 2022})
        answer = await getStudentSubjectScoreController(req)

        body: SubjectScores = answer.body

        assert type(body.tests) is list
        assert len(body.tests) == 1

        assert type(body.works) is list
        assert len(body.works) == 4

        assert type(body.subs) is list
        assert len(body.subs) == 1

        assert body.name == "Ciencia de dados"

        assert body.finalScore == 6.9

        assert body.isPartialScore is True

        assert answer.status_code == 200
