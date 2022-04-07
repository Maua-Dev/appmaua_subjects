from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.enums.evaluation_type import EvaluationType

class GetCourseNameByStudentId:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idStudent: int) -> str:
        try:

            if idStudent is None:
                raise Exception('idStudent is None')

            name = await self._subjectRepository.getStudentCourseName(idStudent)
            if name is None:
                raise Exception('idStudent is invalid')

            return name

        except Exception as error:
            raise UnexpectedError('GetCourseByStudentId', str(error))
