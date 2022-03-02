import pytest

from src.domain.usecases.get_subject_evaluation_weight_usecase import GetSubjectEvaluationWeightUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetSubjectEvaluationWeightUsecase:

    _getSubjectEvaluationWeightUsecase = GetSubjectEvaluationWeightUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_eval_weight_1(self):

        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 1)

        assert weight == 4

    @pytest.mark.asyncio
    async def test_get_eval_weight_2(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 2)

        assert weight == 6

    @pytest.mark.asyncio
    async def test_get_eval_weight_3(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 7)

        assert weight == 1

    @pytest.mark.asyncio
    async def test_get_eval_weight_4(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 8)

        assert weight == 1

    @pytest.mark.asyncio
    async def test_get_eval_weight_5(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 9)

        assert weight == 2

    @pytest.mark.asyncio
    async def test_get_eval_weight_6(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 10)

        assert weight == 2

    @pytest.mark.asyncio
    async def test_get_eval_weight_7(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 19)

        assert weight == 4

    @pytest.mark.asyncio
    async def test_get_eval_weight_8(self):
        weight = await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 20)

        assert weight == 6

    @pytest.mark.asyncio
    async def test_get_eval_weight_error_1(self):

        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationWeightUsecase('acm505', 2022, 1)

    @pytest.mark.asyncio
    async def test_get_eval_weight_error_2(self):
        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationWeightUsecase('ecm505', 2022, 100)

    @pytest.mark.asyncio
    async def test_get_eval_weight_error_3(self):
        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationWeightUsecase('ecm505', None, 1)
