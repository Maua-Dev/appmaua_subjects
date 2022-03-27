
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetCountStudentsBySubjectUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idSubject:int) -> int:
        try:

            if idSubject is None:
                raise Exception('idSubject is None')
            if type(idSubject) is not int:

                raise Exception('idSubject must be an int')

            return await self._subjectRepository.getCountStudentsBySubject(idSubject)

        except Exception as error:
            raise UnexpectedError('GetCountStudentsBySubject', str(error))
