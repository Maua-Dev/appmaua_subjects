from typing import List

from src.domain.entities.grade import Grade
from src.domain.entities.subject import Subject
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.enums.evaluation_type import EvaluationType


class SubjectRepositoryMock(ISubjectRepository):
    def __init__(self) -> None:
        super().__init__()
        self._studentsSubjects = [
            {
                'idSubject': 1,
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 2,
                'idStudent': 1,
                'codeSubject': 'ECM502',
                'name': 'Devops'
            },
            {
                'idSubject': 1,
                'idStudent': 2,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 5,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'name': 'Banco de dados'
            },
            {
                'idSubject': 6,
                'idStudent': 2,
                'codeSubject': 'ECM503',
                'name': 'Controladores'
            },
            {
                'idSubject': 1,
                'idStudent': 3,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 6,
                'idStudent': 3,
                'codeSubject': 'ECM503',
                'name': 'Controladores'
            },
            {
                'idSubject': 3,
                'idStudent': 3,
                'codeSubject': 'ECM504',
                'name': 'IA'
            },
            {
                'idSubject': 1,
                'idStudent': 4,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 2,
                'idStudent': 4,
                'codeSubject': 'ECM502',
                'name': 'Devops'
            },
            {
                'idSubject': 5,
                'idStudent': 4,
                'codeSubject': 'ECM505',
                'name': 'Banco de dados'
            },
            {
                'idSubject': 1,
                'idStudent': 5,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 2,
                'idStudent': 5,
                'codeSubject': 'ECM502',
                'name': 'Devops'
            },
            {
                'idSubject': 3,
                'idStudent': 5,
                'codeSubject': 'ECM504',
                'name': 'IA'
            }
        ]

        self._professorSubjects = [
            {
                'idSubject': 1,
                'idProfessor': 1,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 2,
                'idProfessor': 1,
                'codeSubject': 'ECM502',
                'name': 'Devops'
            },
            {
                'idSubject': 3,
                'idProfessor': 1,
                'codeSubject': 'ECM504',
                'name': 'IA'
            },
            {
                'idSubject': 1,
                'idProfessor': 2,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'idSubject': 5,
                'idProfessor': 2,
                'codeSubject': 'ECM505',
                'name': 'Banco de dados'
            },
            {
                'idSubject': 6,
                'idProfessor': 2,
                'codeSubject': 'ECM503',
                'name': 'Controladores'
            }
        ]

        self._subjects = [
            {
                'id': 1,
                'codeSubject': 'ECM501',
                'name': 'Ciencia de dados'
            },
            {
                'id': 2,
                'codeSubject': 'ECM502',
                'name': 'Devops'
            },
            {
                'id': 3,
                'codeSubject': 'ECM504',
                'name': 'IA'
            },
            {
                'id': 4,
                'codeSubject': 'ECM505',
                'name': 'Banco de dados'
            },
            {
                'id': 6,
                'codeSubject': 'ECM503',
                'name': 'Controladores'
            }
        ]

        self._grades = [
            {
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'grade': Grade(value=6.0, idGrade=5, academicYear=2022, evaluationType=EvaluationType.P1)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'grade': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.PS1)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'grade': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.T1)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'grades': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.P1)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'grade': Grade(value=7.0, idGrade=5, academicYear=2022, evaluationType=EvaluationType.P2)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'grade': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.PS1)
            },
            {
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'grade': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.T1)
            },
            {
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'grades': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.P1)
            },
            {
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'grades': Grade(value=7.0, idGrade=5, academicYear=2022, evaluationType=EvaluationType.P2)
            },
            {
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'grades': Grade(value=9.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.PS1)
            },
            {
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'grades': Grade(value=4.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.T1)
            },
            {
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'grades': Grade(value=8.5, idGrade=5, academicYear=2022, evaluationType=EvaluationType.T2)
            }
        ]

    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:

        subjects = [Subject(codeSubject=row['codeSubject'], name=row['name']) for row in self._studentsSubjects
                    if row['idStudent'] == idStudent]

        return subjects if len(subjects) > 0 else None

    async def getSubjectStudents(self, codeSubject: str) -> List[int]:

        students = [row['idStudent'] for row in self._studentsSubjects
                    if row['codeSubject'].upper() == codeSubject.upper()]

        return students if len(students) > 0 else None

    async def getAllSubjects(self) -> List[Subject]:

        subjects = [Subject(codeSubject=row['codeSubject'], name=row['name']) for row in self._subjects]

        return subjects if len(subjects) > 0 else None

    async def getSubjectByCode(self, codeSubject: str) -> Subject:

        try:
            return [Subject(codeSubject=row['codeSubject'], name=row['name']) for row in self._subjects
                        if row['codeSubject'] == codeSubject][0]
        except IndexError as error:
            return None

    async def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:

        subjects = [Subject(codeSubject=row['codeSubject'], name=row['name']) for row in self._professorSubjects
                    if row['idProfessor'] == idProfessor]
        return subjects if len(subjects) > 0 else None


    async def getNumStudentsByGrades(self, gradeValue:float, codeSubject: str, academicYear: int) -> int:

        numStudents = len([row['grade'].value for row in self._grades if row['grade'].value == gradeValue and
                           row['codeSubject'].upper() == codeSubject.upper()
                           and row['grade'].academicYear == academicYear])

        return numStudents if numStudents > 0 else None