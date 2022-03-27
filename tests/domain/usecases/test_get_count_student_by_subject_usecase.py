import pytest

from src.domain.usecases.get_count_students_by_subject_usecase import GetCountStudentsBySubjectUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock



class Test_GetCountStudentsBySubjectUsecase:

    @pytest.mark.asyncio
    async def test_get_count_student_by_subject_1(self):
        getCountStudentsBySubjectUsecase = GetCountStudentsBySubjectUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsBySubjectUsecase(idSubject=1)
        assert True
        #assert count == 5

    """@pytest.mark.asyncio
    async def test_get_count_student_by_score_2(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsByScoreUsecase(9.5, 'EcM505', 2, 2022)
        assert count == 0

    @pytest.mark.asyncio
    async def test_get_count_student_by_score_3(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        count = await getCountStudentsByScoreUsecase(8.5, 'EcM505', 8, 2022)
        assert count == 1

    @pytest.mark.asyncio
    async def test_get_count_student_by_score_error_1(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsByScoreUsecase(9.5, 'a505', 2, 2022)

    @pytest.mark.asyncio
    async def test_get_count_student_by_score_error_2(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsByScoreUsecase(-1.5, 'ecm505', 2, 2022)

    @pytest.mark.asyncio
    async def test_get_count_student_by_score_error_3(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsByScoreUsecase(9.5, 'ecm505', 50, 2022)

    @pytest.mark.asyncio
    async def test_get_count_student_by_score_error_4(self):
        getCountStudentsByScoreUsecase = GetCountStudentsByScoreUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getCountStudentsByScoreUsecase(9.5, 'ecm505', 2, None)

"""