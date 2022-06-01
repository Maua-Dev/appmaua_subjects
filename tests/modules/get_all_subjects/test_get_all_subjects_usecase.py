import pytest

from src.helpers.errors.domain_errors import NoItemsFound
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_all_subjects.get_all_subjects_usecase import GetAllSubjectsUsecase


class Test_GetAllSubjectsUsecase:

    @pytest.mark.asyncio
    async def test_get_all_subjects_usecase(self):
        repo = SubjectRepositoryMock()
        usecase = GetAllSubjectsUsecase(repo)
        subjects = await usecase()

        assert len(subjects) == len(repo.subjects)
        for s in repo.subjects:
            assert s in subjects

    @pytest.mark.asyncio
    async def test_get_all_subjects_usecase_no_subjects(self):
        repo = SubjectRepositoryMock()
        repo.subjects = []
        usecase = GetAllSubjectsUsecase(repo)
        with pytest.raises(NoItemsFound):
            await usecase()
