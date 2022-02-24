from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetCountStudentsByScoreUsecase:

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

            subject = await self._subjectRepository.getSubjectByCode(codeSubject.upper())
            if subject is None:
                raise Exception('codeSubject is invalid')

            return await self._subjectRepository.getCountStudentsByScore(gradeValue, codeSubject,
                                                                                idEvaluationType, academicYear)

        except Exception as error:
            raise UnexpectedError('GetCountStudentsByScore', str(error))
