from typing import List
from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class StudentSubjectRepositoryMock(ISubjectRepository):
    def __init__(self) -> None:
        super().__init__()
        self._studentsSubjects = [
            {
                'idStudent': 1,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=2, codeSubject='ECM502', name='Devops')
                ]
            },
            {
                'idStudent': 2,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=5, codeSubject='ECM505', name='Banco de dados'),
                    Subject(id=6, codeSubject='ECM503', name='Controladores')
                ]
            }
            ,
            {
                'idStudent': 3,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=6, codeSubject='ECM503', name='Controladores'),
                    Subject(id=3, codeSubject='ECM504', name='IA')
                ]
            }
            ,
            {
                'idStudent': 4,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=2, codeSubject='ECM502', name='Devops'),
                    Subject(id=5, codeSubject='ECM505', name='Banco de dados')
                ]
            }
            ,
            {
                'idStudent': 5,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=2, codeSubject='ECM502', name='Devops'),
                    Subject(id=3, codeSubject='ECM504', name='IA')
                ]
            },
            {
                'idStudent': 6,
                'subjects': []
            }
        ]

        self._professorSubjects = [
            {
                'idProfessor': 1,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=2, codeSubject='ECM502', name='Devops'),
                    Subject(id=3, codeSubject='ECM504', name='IA')
                ]
            },
            {
                'idProfessor': 2,
                'subjects': [
                    Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
                    Subject(id=5, codeSubject='ECM505', name='Banco de dados'),
                    Subject(id=6, codeSubject='ECM503', name='Controladores')
                ]
            }
            ,
            {
                'idProfessor': 3,
                'subjects': []
            }
        ]

        self._subjects = [
            Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
            Subject(id=2, codeSubject='ECM502', name='Devops'),
            Subject(id=3, codeSubject='ECM504', name='IA'),
            Subject(id=5, codeSubject='ECM505', name='Banco de dados'),
            Subject(id=6, codeSubject='ECM503', name='Controladores')
        ]

    def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        subjects: List[Subject] = None
        subjects = [relation['subjects'] for relation in self._studentsSubjects if relation['idStudent'] == idStudent]
        return subjects

    def getSubjectStudents(self, codeSubject: str) -> List[int]:
        subject: Subject
        students: List[int] = None
        students = [relation['idStudent'] for relation in self._studentsSubjects if codeSubject in [subject.codeSubject for subject in relation['subjects']]]
        return students

    def getAllSubjects(self) -> List[Subject]:
        return self._subjects

    def getSubjectByCode(self, codeSubject: str) -> Subject:
        subject: Subject = None
        for subject in self._subjects:
            if subject.codeSubject.upper() == codeSubject.upper():
                subject = subject
        return subject

    def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:
        subjects: List[Subject] = None
        subjects = [relation['subjects'] for relation in self._professorSubjects if relation['idProfessor'] == idProfessor]
        return subjects