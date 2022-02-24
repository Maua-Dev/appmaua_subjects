from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetCountStudentsByScore:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, gradeValue:float, codeSubject: str, idEvaluationType: int,
                                     academicYear: int) -> int:
        try:

            if codeSubject is None:
                raise Exception('idSubject is None')
            if gradeValue is None:
                raise Exception('value is None')
            if idEvaluationType not in range(1, 18):
                raise Exception('idEvaluationType is invalid')
            if academicYear is None:
                raise Exception('academicYear is None')

            numStudents = await self._subjectRepository.getCountStudentsByScore(gradeValue, codeSubject,
                                                                                idEvaluationType, academicYear)

            return numStudents

        except NoItemsFound:
            raise NoItemsFound('GetCountStudentsByScore')

        except Exception as error:
            raise UnexpectedError('GetCountStudentsByScore', str(error))
