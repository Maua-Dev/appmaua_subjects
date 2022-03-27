import pytest

from src.domain.usecases.get_count_students_by_subject_usecase import GetCountStudentsBySubjectUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock



class Test_GetCountStudentsBySubjectUsecase:

    @pytest.mark.asyncio
    async def test_get_count_student_by_subject_1(self):
        getCountStudentsBySubjectUsecase = GetCountStudentsBySubjectUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsBySubjectUsecase(idSubject=1)
        assert count == 5

    @pytest.mark.asyncio
    async def test_get_count_student_by_subject_2(self):
        getCountStudentsBySubjectUsecase = GetCountStudentsBySubjectUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsBySubjectUsecase(idSubject=2)
        assert count == 3

    @pytest.mark.asyncio
    async def test_get_count_student_by_subject_3(self):
        getCountStudentsBySubjectUsecase = GetCountStudentsBySubjectUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsBySubjectUsecase(idSubject=5)
        assert count == 2

    @pytest.mark.asyncio
    async def test_get_count_student_by_subject_error(self):
        getCountStudentsBySubjectUsecase = GetCountStudentsBySubjectUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsBySubjectUsecase("txt")


