import pytest

from src.domain.usecases.get_count_students_by_course_usecase import GetCountStudentsByCourseUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock



class Test_GetCountStudentsByCourseUsecase:

    @pytest.mark.asyncio
    async def test_get_count_student_by_course_1(self):
        getCountStudentsByCourseUsecase = GetCountStudentsByCourseUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsByCourseUsecase(idCourse=1, courseYear=2)
        assert count == 5


    @pytest.mark.asyncio
    async def test_get_count_student_by_course_2(self):
        getCountStudentsByCourseUsecase = GetCountStudentsByCourseUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsByCourseUsecase(idCourse=2, courseYear=1)
        assert count == 3

    @pytest.mark.asyncio
    async def test_get_count_student_by_course_type(self):
        getCountStudentsByCourseUsecase = GetCountStudentsByCourseUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsByCourseUsecase(idCourse=3, courseYear=3)
        assert type(count) == int

    @pytest.mark.asyncio
    async def test_get_count_student_by_course_error(self):
        getCountStudentsByCourseUsecase = GetCountStudentsByCourseUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsByCourseUsecase(idCourse="txt", courseYear=2)


