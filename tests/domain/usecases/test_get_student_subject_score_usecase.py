import pytest

from src.domain.usecases.get_student_subject_score_usecase import GetStudentSubjectScoreUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentSubjectScoreUsecase:

    _getStudentSubjectScoreUsecase = GetStudentSubjectScoreUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_score_1(self):
        score = await self._getStudentSubjectScoreUsecase('ecm505', 2, 2022, 2)

        assert score == 7.0
        # {
        # 'idGrade': 9,
        # 'idStudent': 2,
        # 'codeSubject': 'ECM505',
        # 'value': 7.0,
        # 'academicYear': 2022,
        # 'idEvaluationType': 2
        # }

    @pytest.mark.asyncio
    async def test_get_score_2(self):
        score = await self._getStudentSubjectScoreUsecase('ecm505', 2, 2022, 7)

        assert score == -2
        # {
        #     'idGrade': 11,
        #     'idStudent': 2,
        #     'codeSubject': 'ECM505',
        #     'value': -2,
        #     'academicYear': 2022,
        #     'idEvaluationType': 7
        # }

    @pytest.mark.asyncio
    async def test_get_score_does_not_exist(self):
        score = await self._getStudentSubjectScoreUsecase('ecm505', 6, 2022, 7)

        assert score is None

    @pytest.mark.asyncio
    async def test_get_score_subject_does_not_exist(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', 2, 2022, 7)

    @pytest.mark.asyncio
    async def test_get_score_subject_does_not_exist(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', 2, 2022, 7)

    @pytest.mark.asyncio
    async def test_get_score_eval_type_does_not_exist(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', 2, 2022, 50)

    @pytest.mark.asyncio
    async def test_get_score_error_1(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase(None, 2, 2022, 7)

    @pytest.mark.asyncio
    async def test_get_score_error_2(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', None, 2022, 7)

    @pytest.mark.asyncio
    async def test_get_score_error_3(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', 2, None, 7)

    @pytest.mark.asyncio
    async def test_get_score_error_4(self):
        with pytest.raises(UnexpectedError):
            await self._getStudentSubjectScoreUsecase('ecm506', 2, 2022, None)
