from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetSubjectByCodeUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, codeSubject: str) -> Subject:
        try:
            if codeSubject is None:
                raise Exception('idSubject is None')

            subject = await self._subjectRepository.getSubjectByCode(codeSubject=codeSubject.upper())

            if subject is None:
                raise NoItemsFound('')

            return subject

        except NoItemsFound:
            raise NoItemsFound('GetSubjectByCodeUsecase')

        except Exception as error:
            raise UnexpectedError('GetSubjectByCodeUsecase', str(error))