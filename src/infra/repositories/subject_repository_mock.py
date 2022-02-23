from typing import List

from src.domain.entities.grade import Grade
from src.domain.entities.subject import Subject
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository


class SubjectRepositoryMock(ISubjectRepository):
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
            Subject(id=1, codeSubject='ECM501', name='Ciencia de dados', grades=[Grade(value=6.0,idGrade=1,idStudent=1,codeSubject='ECM501'),
                                                                                 Grade(value=6.0,idGrade=2,idStudent=2,codeSubject='ECM501'),
                                                                                 Grade(value=6.0,idGrade=3,idStudent=3,codeSubject='ECM501'),
                                                                                 Grade(value=3.0,idGrade=4,idStudent=4,codeSubject='ECM501'),
                                                                                 Grade(value=9.5,idGrade=5,idStudent=5,codeSubject='ECM501')])),
            Subject(id=2, codeSubject='ECM502', name='Devops', grades=[Grade(value=6.0, idGrade=1, idStudent=1, codeSubject='ECM502'),
                                                                       Grade(value=10.0, idGrade=2, idStudent=4, codeSubject='ECM502'),
                                                                       Grade(value=1.5, idGrade=3, idStudent=5, codeSubject='ECM502')])),
            Subject(id=3, codeSubject='ECM504', name='IA', grades=[Grade(value=4.0, idGrade=1, idStudent=3, codeSubject='ECM504'),
                                                                   Grade(value=6.0, idGrade=2, idStudent=5, codeSubject='ECM504')]),
            Subject(id=5, codeSubject='ECM505', name='Banco de dados', grades=[Grade(value=2.0, idGrade=1, idStudent=2, codeSubject='ECM505'),
                                                                               Grade(value=1.0, idGrade=2, idStudent=4, codeSubject='ECM505')]),
            Subject(id=6, codeSubject='ECM503', name='Controladores', grades=[Grade(value=10.0, idGrade=1, idStudent=3, codeSubject='ECM503'),
                                                                              Grade(value=1.0, idGrade=2, idStudent=2, codeSubject='ECM503')])
        ]

    value: float
    idGrade: int
    idStudent: int
    codeSubject: str
    def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        try:
            subjects: List[Subject] = None
            subjects = [relation['subjects'] for relation in self._studentsSubjects if relation['idStudent'] == idStudent][0]

            if len(subjects) > 0:
                return subjects
            else:
                return None

        except IndexError as error:
            return None

    def getSubjectStudents(self, codeSubject: str) -> List[Subject]:
        subject: Subject
        students: List[int] = None
        students = [relation['idStudent'] for relation in self._studentsSubjects if codeSubject in [subject.codeSubject for subject in relation['subjects']]]
        if len(students) > 0:
            return students
        else:
            return None

    def getAllSubjects(self) -> List[Subject]:
        if len(self._subjects) > 0:
            return self._subjects, len(self._subjects)
        else:
            return None, 0

    def getSubjectByCode(self, codeSubject: str) -> Subject:
        subject: Subject = None
        for subjectx in self._subjects:
            if subjectx.codeSubject.upper() == codeSubject.upper():
                subject = subjectx
        return subject

    def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        try:
            subjects: List[Subject] = None
            subjects = [relation['subjects'] for relation in self._professorSubjects if relation['idProfessor'] == idProfessor][0]
            if len(subjects) > 0:
                return subjects, len(subjects)
            else:
                return None, 0

        except IndexError as error:
            return None, 0
