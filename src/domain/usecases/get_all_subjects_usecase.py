from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetAllSubjectsUsecase:

    def __init__(self, subjectRepository: ISubjectRepository):
        self._subjectRepository = subjectRepository

    def __call__(self):
        try:
            subjects = self._subjectRepository.getAllSubjects()

            if subjects is None:
                raise Exception('Nenhuma matéria encontrada.')

            return subjects

        except Exception as error:
            raise UnexpectedError('GetAllSubjects', str(error))


