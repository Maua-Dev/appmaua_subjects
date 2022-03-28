import pytest
from src.domain.usecases.get_subject_by_professor_id_usecase import GetSubjectByProfessorIdUsecase
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.entities.subject import Subject
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetSubjectByProfessorIdUsecase:

    @pytest.mark.asyncio
    async def test_get_professor_subjects_1(self):
        getSubjectByProfessorIdUsecase = GetSubjectByProfessorIdUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = await getSubjectByProfessorIdUsecase(1)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in subjects
        assert Subject(id=3, codeSubject='ECM504', name='IA') in subjects

    @pytest.mark.asyncio
    async def test_get_professor_subjects_2(self):
        getSubjectByProfessorIdUsecase = GetSubjectByProfessorIdUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = await getSubjectByProfessorIdUsecase(2)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=5, codeSubject='ECM505', name='Banco de dados') in subjects
        assert Subject(id=6, codeSubject='ECM503', name='Controladores') in subjects

    @pytest.mark.asyncio
    async def test_get_professor_subjects_empty(self):
        getSubjectByProfessorIdUsecase = GetSubjectByProfessorIdUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(NoItemsFound):
            await getSubjectByProfessorIdUsecase(0)

    @pytest.mark.asyncio
    async def test_get_professor_subjects_error(self):
        getSubjectByProfessorIdUsecase = GetSubjectByProfessorIdUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            await getSubjectByProfessorIdUsecase(None)
