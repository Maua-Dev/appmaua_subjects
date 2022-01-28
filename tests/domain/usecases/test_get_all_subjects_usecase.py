import pytest

from src.domain.entities.subject import Subject
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock

class Test_GetAllSubjectsUsecase:

    def test_get_all_subjects(self):
        getAllSubjectsUsecase = GetAllSubjectsUsecase(subjectRepository=SubjectRepositoryMock())
        subjects, count = getAllSubjectsUsecase()
        assert len(subjects) > 0
        assert len(subjects) == 5
        assert Subject(id=1, codeSubject='ECM501', name='Ciencia de dados') in subjects
        assert Subject(id=2, codeSubject='ECM502', name='Devops') in subjects
        assert Subject(id=3, codeSubject='ECM504', name='IA') in subjects
        assert Subject(id=5, codeSubject='ECM505', name='Banco de dados') in subjects
        assert Subject(id=6, codeSubject='ECM503', name='Controladores') in subjects
