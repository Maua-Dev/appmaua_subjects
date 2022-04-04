import pytest
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentCourseYearUsecase:

    @pytest.mark.asyncio
    async def test_get_student_course_year_1(self):
        getStudentCourseYearUsecase = GetStudentCourseYearUsecase(subjectRepository=SubjectRepositoryMock())
        courseYear = await getStudentCourseYearUsecase(1, academicYear=2022)
        assert courseYear == 2

    @pytest.mark.asyncio
    async def test_get_student_course_year_2(self):
        getStudentCourseYearUsecase = GetStudentCourseYearUsecase(subjectRepository=SubjectRepositoryMock())
        courseYear = await getStudentCourseYearUsecase(9, academicYear=2022)
        assert courseYear == 3



    @pytest.mark.asyncio
    async def test_get_student_course_year_error(self):
        getStudentCourseYearUsecase = GetStudentCourseYearUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getStudentCourseYearUsecase(None, academicYear=2022)
