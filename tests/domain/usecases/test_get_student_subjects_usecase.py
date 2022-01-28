import pytest

from src.domain.entities.subject import Subject
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.errors.errors import UnexpectedError
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentSubjectsUsecase:

    def test_get_student_subjects(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects = getStudentSubjectsUsecase(1)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in subjects

    def test_get_student_subjects_empty(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            getStudentSubjectsUsecase(0)

    def test_get_student_subjects_error(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            getStudentSubjectsUsecase(idStudent=None)
