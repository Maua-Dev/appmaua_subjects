from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.helpers.errors.domain_errors import NoItemsFound
from src.domain.entities.subject import Subject

class GetSubjectUsecase:

    def __init__(self, repo: ISubjectRepository):
        self.repo = repo

    async def __call__(self, ra: str, code: str) -> Subject:
        subject = await self.repo.get_subject(ra=ra, code=code)

        if subject == None:
            raise NoItemsFound('get_subject')

        return subject
