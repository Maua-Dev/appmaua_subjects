import pytest

from src.domain.usecases.get_subject_evaluation_quantity_usecase import GetSubjectEvaluationQuantityUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetSubjectEvaluationQuantityUsecase:

    _getSubjectEvaluationQuantityUsecase = GetSubjectEvaluationQuantityUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_subj_test_qnt_1(self):

        qnt = await self._getSubjectEvaluationQuantityUsecase('ecm505', 2022, 20)

        assert qnt == 2

    @pytest.mark.asyncio
    async def test_get_subj_work_qnt_2(self):
        qnt = await self._getSubjectEvaluationQuantityUsecase('ecm505', 2022, 19)

        assert qnt == 4

    @pytest.mark.asyncio
    async def test_get_subj_psub_qnt_3(self):
        qnt = await self._getSubjectEvaluationQuantityUsecase('ecm505', 2022, 21)

        assert qnt == 1

    @pytest.mark.asyncio
    async def test_get_subj_psub_qnt_1(self):

        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationQuantityUsecase('acm505', 2022, 20)

    @pytest.mark.asyncio
    async def test_get_subj_psub_qnt_2(self):
        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationQuantityUsecase('ecm505', None, 20)

    @pytest.mark.asyncio
    async def test_get_subj_psub_qnt_3(self):
        with pytest.raises(UnexpectedError):
            await self._getSubjectEvaluationQuantityUsecase('ecm505', 2022, 2)
