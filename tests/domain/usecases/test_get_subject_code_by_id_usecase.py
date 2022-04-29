import pytest

from src.domain.usecases.get_subject_code_by_id_usecase import GetSubjectCodeByIdUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock

class Test_GetSubjectCodeByIdUsecase:

    _GetSubjectCodeByIdUsecase = GetSubjectCodeByIdUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_code_test_1(self):

        qnt = await self._GetSubjectCodeByIdUsecase(1)

        assert qnt == 'ECM501'

    @pytest.mark.asyncio
    async def test_get_code_test_2(self):
        qnt = await self._GetSubjectCodeByIdUsecase(3)

        assert qnt == 'ECM504'

    @pytest.mark.asyncio
    async def test_get_code_test_3(self):
        qnt = await self._GetSubjectCodeByIdUsecase(5)

        assert qnt == 'ECM505'

    @pytest.mark.asyncio
    async def test_get_code_eval_error_1(self):

        with pytest.raises(UnexpectedError):
            await self._GetSubjectCodeByIdUsecase(None)

    @pytest.mark.asyncio
    async def test_get_code_eval_error_2(self):
        with pytest.raises(UnexpectedError):
            await self._GetSubjectCodeByIdUsecase(-1)

    @pytest.mark.asyncio
    async def test_get_code_eval_error_3(self):
        with pytest.raises(UnexpectedError):
            await self._GetSubjectCodeByIdUsecase(0)
