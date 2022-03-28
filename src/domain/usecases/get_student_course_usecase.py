from typing import List, Tuple
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetStudentCourseUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idStudent: int) -> Tuple[int, int]:
        try:
            if idStudent is None:
                raise Exception('idStudent is None')
            if type(idStudent) is not int:
                raise Exception('idStudent must be an int')

            tp = await self._subjectRepository.getStudentCourse(idStudent=idStudent)



            return tp

        except Exception as error:
            raise UnexpectedError('GetStudentCourseUsecase', str(error))
