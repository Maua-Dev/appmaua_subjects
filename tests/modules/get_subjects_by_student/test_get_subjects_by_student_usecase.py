import pytest
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_subjects_by_student.get_subjects_by_student_usecase import GetSubjectsByStudentUsecase


class Test_GetSubjectsByStudentUsecase:

    @pytest.mark.asyncio
    async def test_get_subjects_by_student_usecase(self):
        repo = SubjectRepositoryMock()
        usecase = GetSubjectsByStudentUsecase(repo)
        subjects = await usecase(ra="19003315")

        assert len(subjects) == 2
        for subject in repo.students[0].subjects:
            assert subject in subjects