from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.enums.evaluation_type import EvaluationType

class GetSubjectNameByIdUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idSubject: int) -> str:
        try:

            if idSubject is None:
                raise Exception('idSubject is None')

            name = await self._subjectRepository.getSubjectNameById(idSubject)
            if name is None:
                raise Exception('idSubject is invalid')

            return name

        except Exception as error:
            raise UnexpectedError('GetSubjectNameByIdUsecase', str(error))
