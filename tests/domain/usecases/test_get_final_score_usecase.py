import pytest

from src.domain.usecases.get_final_score_usecase import GetFinalScoreUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetCountStudentsByScoreUsecase:

    _getFinalScoreUsecase = GetFinalScoreUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_student_score_1(self):

        score, isFinal = await self._getFinalScoreUsecase('ecm501', 2022, 1)
        assert score == 6.9
        assert isFinal is True

    @pytest.mark.asyncio
    async def test_get_student_score_2(self):

        score, isFinal = await self._getFinalScoreUsecase('ecm505', 2022, 2)
        assert score == 6.2  # Avalia se realmente esta truncando (sem truncar seria 6.26667)
        assert isFinal is True

    @pytest.mark.asyncio
    async def test_get_student_score_3(self):

        score, isFinal = await self._getFinalScoreUsecase('ecm505', 2022, 1)
        assert score == 8.9  # Avalia se realmente esta truncando (sem truncar seria 6.26667)
        assert isFinal is False

    @pytest.mark.asyncio
    async def test_get_student_score_error_1(self):

        with pytest.raises(UnexpectedError):
            await self._getFinalScoreUsecase('acm505', 2022, 1)

    @pytest.mark.asyncio
    async def test_get_student_score_error_2(self):

        with pytest.raises(UnexpectedError):
            await self._getFinalScoreUsecase('ecm505', None, 1)

    @pytest.mark.asyncio
    async def test_get_student_score_error_3(self):

        with pytest.raises(UnexpectedError):
            await self._getFinalScoreUsecase('ecm505', 2022, None)
