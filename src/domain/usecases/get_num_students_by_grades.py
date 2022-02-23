from typing import List
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject


class GetNumStudensByGrades:

    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository

    def __call__(self, value:int, codeSubject: str) -> int:
        try:
            if codeSubject is None and value is None:
                raise Exception('idSubject and value is None')
            elif codeSubject is None:
                raise Exception('idSubject is None')
            elif value is None:
                raise Exception('value is None')

            subject = self._subjectRepository.getSubjectByCode(codeSubject)
            numStudents = 0
            for grade in subject.grades:
                if grade.value == value:
                    numStudents += 1

            if subject is None:
                raise NoItemsFound('')

            return numStudents

        except NoItemsFound:
            raise NoItemsFound('GetAllSubjects')

        except Exception as error:
            raise UnexpectedError('GetNumStudentsByGrade', str(error))