import pytest

from src.domain.usecases.get_subject_name_by_id_usecase import GetSubjectNameByIdUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock

class Test_GetSubjectNameByIdUsecase:

    _GetCourseNameByStudentIdUsecase = GetSubjectNameByIdUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_name_test_1(self):

        qnt = await self._GetCourseNameByStudentIdUsecase(1)

        assert qnt == 'Ciencia de dados'

    @pytest.mark.asyncio
    async def test_get_name_test_2(self):
        qnt = await self._GetCourseNameByStudentIdUsecase(3)

        assert qnt == 'IA'

    @pytest.mark.asyncio
    async def test_get_name_test_3(self):
        qnt = await self._GetCourseNameByStudentIdUsecase(5)

        assert qnt == 'Controladores'

    @pytest.mark.asyncio
    async def test_get_name_eval_error_1(self):

        with pytest.raises(UnexpectedError):
            await self._GetCourseNameByStudentIdUsecase(None)

    @pytest.mark.asyncio
    async def test_get_name_eval_error_2(self):
        with pytest.raises(UnexpectedError):
            await self._GetCourseNameByStudentIdUsecase(-1)

    @pytest.mark.asyncio
    async def test_get_name_eval_error_3(self):
        with pytest.raises(UnexpectedError):
            await self._GetCourseNameByStudentIdUsecase(0)
