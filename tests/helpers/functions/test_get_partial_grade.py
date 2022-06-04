import pytest

from src.helpers.functions import getPartialGrade
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_getPartialGrade:
    async def test_get_current_grade(self):
        repo = SubjectRepositoryMock()

        subject1 = repo.subjects[0]
        subject2 = repo.subjects[1]

        grade1 = await getPartialGrade(subject1.grades)
        grade2 = await getPartialGrade(subject2.grades)

        assert grade1 > 6.2 and grade1 < 6.3
        assert grade2 == 3