import pytest
from src.domain.usecases.get_student_course_id_usecase import GetStudentCourseIdUsecase
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentCourseIdUsecase:

    @pytest.mark.asyncio
    async def test_get_student_course_id_1(self):
        getStudentCourseIdUsecase = GetStudentCourseIdUsecase(subjectRepository=SubjectRepositoryMock())
        idCourse = await getStudentCourseIdUsecase(1, 2022)
        assert idCourse == 1

    @pytest.mark.asyncio
    async def test_get_student_course_id_2(self):
        getStudentCourseIdUsecase = GetStudentCourseIdUsecase(subjectRepository=SubjectRepositoryMock())
        idCourse = await getStudentCourseIdUsecase(9, 2022)
        assert idCourse == 3



    @pytest.mark.asyncio
    async def ttest_get_student_course_id_error(self):
        getStudentCourseIdUsecase = GetStudentCourseIdUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getStudentCourseIdUsecase(None)
