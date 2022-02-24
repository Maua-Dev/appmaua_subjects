from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class GetNumStudensByGrades:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, gradeValue: float, codeSubject: str) -> int:
        try:
            if codeSubject is None and gradeValue is None:
                raise Exception('idSubject and value is None')
            elif codeSubject is None:
                raise Exception('idSubject is None')
            elif gradeValue is None:
                raise Exception('value is None')

            numStudents = self._subjectRepository.getNumStudentsByGrades(gradeValue, codeSubject)

            return numStudents

        except NoItemsFound:
            raise NoItemsFound('GetNumStudensByGrades')

        except Exception as error:
            raise UnexpectedError('GetNumStudentsByGrade', str(error))
