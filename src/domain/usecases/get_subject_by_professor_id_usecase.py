from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetSubjectByProfessorIdUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, idProfessor: int) -> tuple:
        try:
            if idProfessor is None:
                raise Exception('idProfessor is None')

            subjects, count = self._subjectRepository.getSubjectByProfessorId(idProfessor)

            if subjects is None:
                raise NoItemsFound('')

            return subjects, count

        except NoItemsFound:
            raise NoItemsFound('GetAllSubjects')

        except Exception as error:
            raise UnexpectedError('GetSubjectByProfessorId', str(error))
