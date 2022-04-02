from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetCountStudentsByCourseAndYearUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, idCourse:int, courseYear:int, academicYear: int) -> int:
        try:

            if idCourse is None:
                raise Exception('idCourse is None')
            if type(idCourse) is not int:
                raise Exception('idCourse must be an int')

            if courseYear is None:
                raise Exception('courseYear is None')
            if type(courseYear) is not int:
                raise Exception('courseYear must be an int')

            if academicYear is None:
                raise Exception('academicYear is None')
            if type(academicYear) is not int:
                raise Exception('academicYear must be an int')

            return await self._subjectRepository.getCountStudentsByCourse(idCourse=idCourse, courseYear=courseYear,
                                                                          academicYear=academicYear)

        except Exception as error:
            raise UnexpectedError('GetCountStudentsByCourseAndYearUsecase', str(error))
