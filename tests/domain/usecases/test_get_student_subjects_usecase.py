import pytest

from src.domain.entities.subject import Subject
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentSubjectsUsecase:

    @pytest.mark.asyncio
    async def test_get_student_subjects_1(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = await getStudentSubjectsUsecase(1)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in subjects

    
    @pytest.mark.asyncio
    async def test_get_student_subjects_2(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = await getStudentSubjectsUsecase(2)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=5, codeSubject='ECM505', name='Banco de dados') in subjects


    @pytest.mark.asyncio
    async def test_get_student_subjects_empty(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(NoItemsFound):
            await getStudentSubjectsUsecase(0)

    @pytest.mark.asyncio
    async def test_get_student_subjects_error(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getStudentSubjectsUsecase(idStudent=None)
