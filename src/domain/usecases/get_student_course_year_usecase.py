from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetStudentCourseYearUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idStudent: int) -> int:
        try:
            if idStudent is None:
                raise Exception('idStudent is None')

            courseYear = await self._subjectRepository.getStudentCourseYear(idStudent=idStudent)

            return courseYear


        except Exception as error:
            raise UnexpectedError('GetStudentCourseYearUsecase', str(error))
