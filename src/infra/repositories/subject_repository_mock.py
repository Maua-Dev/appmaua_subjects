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
            Subject(id=1, codeSubject='ECM501', name='Ciencia de dados'),
            Subject(id=2, codeSubject='ECM502', name='Devops'),
            Subject(id=3, codeSubject='ECM504', name='IA'),
            Subject(id=5, codeSubject='ECM505', name='Banco de dados'),
            Subject(id=6, codeSubject='ECM503', name='Controladores')
        ]

        self._grades = [
            Grade(value=6.0, idGrade=1, idStudent=1, codeSubject='ECM501'),
            Grade(value=6.0, idGrade=2, idStudent=2, codeSubject='ECM501'),
            Grade(value=6.0, idGrade=3, idStudent=3, codeSubject='ECM501'),
            Grade(value=3.0, idGrade=4, idStudent=4, codeSubject='ECM501'),
            Grade(value=9.5, idGrade=5, idStudent=5, codeSubject='ECM501')
        ]

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
            return None

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
                return subjects
            else:
                return None

        except IndexError as error:
            return None

    def getNumStudentsByGrades(self, gradeValue:float, codeSubject: str) -> int:
        try:
            numStudents = len([grade.value for grade in self._grades if grade.value == gradeValue and grade.codeSubject.upper() == codeSubject.upper()])

            return numStudents

        except IndexError as error:
            return None