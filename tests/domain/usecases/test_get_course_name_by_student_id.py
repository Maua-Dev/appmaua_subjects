import pytest

from src.domain.usecases.get_course_name_by_student_id_usecase import GetCourseNameByStudentIdUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock

class Test_GetCourseNameByStudentIdUsecase:

    _GetCourseNameByStudentIdUsecase = GetCourseNameByStudentIdUsecase(subjectRepository=SubjectRepositoryMock())

    @pytest.mark.asyncio
    async def test_get_name_test_1(self):

        qnt = await self._GetCourseNameByStudentIdUsecase(1)

        assert qnt == 'Engenharia de Computação'

    @pytest.mark.asyncio
    async def test_get_name_test_2(self):
        qnt = await self._GetCourseNameByStudentIdUsecase(6)

        assert qnt == 'Ciclo Básico'

    @pytest.mark.asyncio
    async def test_get_name_test_3(self):
        qnt = await self._GetCourseNameByStudentIdUsecase(9)

        assert qnt == 'Engenharia de Controle e Automação'

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
