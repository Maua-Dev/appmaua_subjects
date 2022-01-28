import pytest

from src.domain.entities.subject import Subject
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Test_GetStudentSubjectsUsecase:

    def test_get_student_subjects_1(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects, count = getStudentSubjectsUsecase(1)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in subjects

    def test_get_student_subjects_2(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects, count = getStudentSubjectsUsecase(2)
        assert len(subjects) > 0
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=5, codeSubject='ECM505', name='Banco de dados') in subjects
        assert Subject(id=6, codeSubject='ECM503', name='Controladores') in subjects


    def test_get_student_subjects_empty(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(NoItemsFound):
            getStudentSubjectsUsecase(0)

    def test_get_student_subjects_error(self):
        getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        with pytest.raises(UnexpectedError):
            getStudentSubjectsUsecase(idStudent=None)
