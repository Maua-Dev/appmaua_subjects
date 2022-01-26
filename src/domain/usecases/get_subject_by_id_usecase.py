from typing import List
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetSubjectByIdUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, idSubject: int) -> List[Subject]:
        try:
            if idSubject is None:
                raise Exception('idSubject is None')
            subjects = self._subjectRepository.getSubjectById(idSubject=idSubject)
            return subjects
        except Exception as error:
            raise UnexpectedError('GetSubjectById', str(error))