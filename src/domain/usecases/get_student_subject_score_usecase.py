from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.enums.evaluation_type import EvaluationType

class GetStudentSubjectScoreUsecase:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    async def __call__(self, codeSubject: str, idStudent: int, academicYear: int, idEvaluationType: int) -> int:
        try:

            if codeSubject is None:
                raise Exception('codeSubject is None')

            if idStudent is None:
                raise Exception('idStudent is None')

            try:
                evalType = EvaluationType(idEvaluationType)
            except Exception:
                raise Exception('idEvaluationType is invalid')

            if academicYear is None:
                raise Exception('academicYear is None')

            subject = await self._subjectRepository.getSubjectByCode(codeSubject.upper())
            if subject is None:
                raise Exception('codeSubject is invalid')

            return await self._subjectRepository.getSubjectScoreByEvalType(codeSubject.upper(), idStudent, academicYear,
                                                                           idEvaluationType)

        except Exception as error:
            raise UnexpectedError('GetCountStudentsByScore', str(error))
