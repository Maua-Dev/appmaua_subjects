from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from typing import List

from src.helpers.errors.domain_errors import NoItemsFound


class GetSubjectsByStudentUsecase:

    def __init__(self, repo: ISubjectRepository):
        self.repo = repo

    async def __call__(self, ra:str) -> List[Subject]:

        subjects = await self.repo.get_subjects_by_student(ra)

        if subjects == None or len(subjects) == 0:
            return NoItemsFound("get_subjects_by_student")

        return subjects
