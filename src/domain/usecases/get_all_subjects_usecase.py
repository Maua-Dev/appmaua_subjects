from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetAllSubjectsUsecase:

    def __init__(self, subjectRepository: ISubjectRepository):
        self._subjectRepository = subjectRepository

    async def __call__(self):
        try:
            subjects = await self._subjectRepository.getAllSubjects()

            if subjects is None:
                raise NoItemsFound('')

            return subjects

        except NoItemsFound:
            raise NoItemsFound('GetAllSubjects')

        except Exception as error:
            raise UnexpectedError('GetAllSubjects', str(error))


