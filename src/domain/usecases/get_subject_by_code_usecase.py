from typing import List
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetSubjectByCodeUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, codeSubject: str) -> Subject:
        try:
            if codeSubject is None:
                raise Exception('idSubject is None')

            subjects = self._subjectRepository.getSubjectByCode(codeSubject=codeSubject)

            if subjects is None:
                raise Exception('Nenhuma matéria encontrada.')

            return subjects

        except Exception as error:
            raise UnexpectedError('GetSubjectById', str(error))