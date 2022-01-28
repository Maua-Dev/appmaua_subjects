from typing import List
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetSubjectByProfessorIdUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, idProfessor: int) -> List[Subject]:
        try:
            if idProfessor is None:
                raise Exception('idProfessor is None')

            subjects = self._subjectRepository.getSubjectByProfessorId(idProfessor=idProfessor)

            if subjects is None:
                raise Exception('Nenhuma matéria encontrada.')

            return subjects

        except Exception as error:
            raise UnexpectedError('GetSubjectByProfessorId', str(error))
