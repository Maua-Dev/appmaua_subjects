import pytest
from typing import List
from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.errors.errors import UnexpectedError

class SubjectRepositoryMock(ISubjectRepository):
    def __init__(self) -> None:
        super().__init__()
        self._studentsSubjects = [
            {
                'idAluno': 1,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'), 
                    Subject(id=2, codeSubject='ECM502', name='Devops')
                ],
                'idAluno': 2,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'), 
                    Subject(id=2, codeSubject='ECM502', name='Devops'),
                    Subject(id=3, codeSubject='ECM503', name='IA')
                ]
            }
        ]
    def getStudentSubjects(self, idAluno: int) -> List[Subject]:
        return filter(lambda subject: subject['idAluno'] == idAluno,self._studentsSubjects)


class Test_GetStudentSubjectsUsecase:

    def test_get_student_subjects(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = getStudentSubjectsUsecase(1)
        assert len(subjects) > 0 
    def test_get_student_subjects_empty(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = getStudentSubjectsUsecase(0)
        assert len(subjects) == 0 
    def test_get_student_subjects_error(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            getStudentSubjectsUsecase(idAluno=None)