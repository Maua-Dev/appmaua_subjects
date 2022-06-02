import pytest

from src.helpers.functions import getCurrentGrade
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_getCurrentGrade:
    async def test_get_current_grade(self):
        repo = SubjectRepositoryMock()

        subject1 = repo.subjects[0]
        subject2 = repo.subjects[1]

        grade1 = await getCurrentGrade(subject1.grades)
        grade2 = await getCurrentGrade(subject2.grades)

        assert grade1 > 1.2 and grade1 < 1.3
        assert grade2 == 0.6