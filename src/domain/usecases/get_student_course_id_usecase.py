from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetStudentCourseIdUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idStudent: int, academicYear: int) -> int:
        try:
            if idStudent is None:
                raise Exception('idStudent is None')
            if type(idStudent) is not int:
                raise Exception('idStudent must be an int')

            if academicYear is None:
                raise Exception('academicYear is None')
            if type(academicYear) is not int:
                raise Exception('academicYear must be an int')

            idCourse = await self._subjectRepository.getStudentCourseId(idStudent=idStudent, academicYear=academicYear)

            return idCourse


        except Exception as error:
            raise UnexpectedError('GetStudentCourseIdUsecase', str(error))
