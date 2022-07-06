from typing import List

from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.helpers.errors.domain_errors import NoItemsFound


class GetAllSubjectsUsecase:
    def __init__(self, repo: ISubjectRepository):
        self.repo = repo

    async def __call__(self) -> List[Subject]:
        subjects = await self.repo.get_all_subjects()

        if subjects is None or len(subjects) == 0:
            raise NoItemsFound('get_all_subjects')

        return subjects
