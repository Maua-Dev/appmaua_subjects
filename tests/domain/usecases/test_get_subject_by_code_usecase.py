import pytest

from src.domain.entities.subject import Subject
from src.domain.errors.errors import NoItemsFound
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock

class Test_GetSubjectByCodeUsecase:

    @pytest.mark.asyncio
    async def test_get_subject_by_code_1(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        subject = await getSubjectByCodeUsecase('EcM505')
        assert subject == Subject(id=5, codeSubject='ECM505', name='Banco de dados')

    @pytest.mark.asyncio
    async def test_get_subject_by_code_2(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        subject = await getSubjectByCodeUsecase('EcM501')
        assert subject == Subject(id=1, codeSubject='ECM501', name='Ciencia de dados')

    @pytest.mark.asyncio
    async def test_get_subject_by_code_3(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        subject = await getSubjectByCodeUsecase('EcM502')
        assert subject == Subject(id=2, codeSubject='ECM502', name='Devops')

    @pytest.mark.asyncio
    async def test_get_subject_by_code_4(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        subject = await getSubjectByCodeUsecase('EcM503')
        assert subject == Subject(id=6, codeSubject='ECM503', name='Controladores')

    @pytest.mark.asyncio
    async def test_get_subject_by_code_5(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        subject = await getSubjectByCodeUsecase('EcM504')
        assert subject == Subject(id=3, codeSubject='ECM504', name='IA')

    @pytest.mark.asyncio
    async def test_get_subject_by_code_error(self):
        getSubjectByCodeUsecase = GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(NoItemsFound):
            await getSubjectByCodeUsecase('ESM504')