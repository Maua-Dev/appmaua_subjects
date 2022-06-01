import pytest

from src.modules.get_subject.get_subject_usecase import GetSubjectUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.helpers.errors.domain_errors import NoItemsFound


class Test_GetSubjectUsecase():
    @pytest.mark.asyncio
    async def test_get_subject_usecase(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectUsecase(repo)
        subject = await usecase(ra="19003315",
                                code="ECM401")

        assert len(subject.code) == 6
        assert subject.name == "Banco de Dados"

    @pytest.mark.asyncio
    async def test_get_subject_usecase_not_found_ra(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectUsecase(repo)
        with pytest.raises(NoItemsFound):
            await usecase(ra="21010757",
                          code="ECM401")

    @pytest.mark.asyncio
    async def test_get_subject_usecase_not_found_code(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectUsecase(repo)
        with pytest.raises(NoItemsFound):
            await usecase(ra="19003315",
                          code="ABC123")
