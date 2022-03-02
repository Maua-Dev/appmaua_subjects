from typing import List

from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository


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
                'idGrade': 1,
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 1

            },
            {
                'idGrade': 2,
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 5
            },
            {
                'idGrade': 3,
                'idStudent': 1,
                'codeSubject': 'ECM505',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 7
            },
            {
                'idGrade': 4,
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 1
            },
            {
                'idGrade': 5,
                'idStudent': 4,
                'codeSubject': 'ECM501',
                'value': -1,
                'academicYear': 2022,
                'idEvaluationType': 1
            },
            {
                'idGrade': 6,
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 5
            },
            {
                'idGrade': 7,
                'idStudent': 1,
                'codeSubject': 'ECM501',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 7
            },
            {
                'idGrade': 8,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 1
            },
            {
                'idGrade': 9,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'value': 7.0,
                'academicYear': 2022,
                'idEvaluationType': 2
            },
            {
                'idGrade': 10,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'value': 9.5,
                'academicYear': 2022,
                'idEvaluationType': 5
            },
            {
                'idGrade': 11,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'value': -2,
                'academicYear': 2022,
                'idEvaluationType': 7
            },
            {
                'idGrade': 12,
                'idStudent': 2,
                'codeSubject': 'ECM505',
                'value': 8.5,
                'academicYear': 2022,
                'idEvaluationType': 8
            }
        ]

        self._evalData = [
            {
                'id': 1,
                'idEvaluationType': 20,
                'codeSubject': 'ECM505',
                'quantity': 2,
                'academicYear': 2022
            },
            {
                'id': 2,
                'idEvaluationType': 19,
                'codeSubject': 'ECM505',
                'quantity': 4,
                'academicYear': 2022
            },
            {
                'id': 3,
                'idEvaluationType': 20,
                'codeSubject': 'ECM501',
                'quantity': 1,
                'academicYear': 2022
            },
            {
                'id': 4,
                'idEvaluationType': 19,
                'codeSubject': 'ECM501',
                'quantity': 4,
                'academicYear': 2022
            },
            {
                'id': 5,
                'idEvaluationType': 21,
                'codeSubject': 'ECM505',
                'quantity': 1,
                'academicYear': 2022
            },
            {
                'id': 6,
                'idEvaluationType': 21,
                'codeSubject': 'ECM505',
                'quantity': 1,
                'academicYear': 2022
            },
            {
                'id': 7,
                'idEvaluationType': 21,
                'codeSubject': 'ECM501',
                'quantity': 1,
                'academicYear': 2022
            },
        ]

        self._evalWeight = [
            {
                'id': 1,
                'idEvaluationType': 1,
                'codeSubject': 'ECM505',
                'weight': 4,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 2,
                'idEvaluationType': 2,
                'codeSubject': 'ECM505',
                'weight': 6,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 3,
                'idEvaluationType': 7,
                'codeSubject': 'ECM505',
                'weight': 1,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 4,
                'idEvaluationType': 8,
                'codeSubject': 'ECM505',
                'weight': 1,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 5,
                'idEvaluationType': 9,
                'codeSubject': 'ECM505',
                'weight': 2,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 6,
                'idEvaluationType': 10,
                'codeSubject': 'ECM505',
                'weight': 2,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 7,
                'idEvaluationType': 1,
                'codeSubject': 'ECM501',
                'weight': 1,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 8,
                'idEvaluationType': 7,
                'codeSubject': 'ECM501',
                'weight': 2,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 9,
                'idEvaluationType': 8,
                'codeSubject': 'ECM501',
                'weight': 3,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 10,
                'idEvaluationType': 20,
                'codeSubject': 'ECM505',
                'weight': 6,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 11,
                'idEvaluationType': 19,
                'codeSubject': 'ECM505',
                'weight': 4,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 12,
                'idEvaluationType': 20,
                'codeSubject': 'ECM501',
                'weight': 5,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 13,
                'idEvaluationType': 19,
                'codeSubject': 'ECM501',
                'weight': 5,
                'academicYear': 2022,
                'replaces': None
            },
            {
                'id': 14,
                'idEvaluationType': 5,
                'codeSubject': 'ECM501',
                'weight': 1,
                'academicYear': 2022,
                'replaces': 1
            },
            {
                'id': 15,
                'idEvaluationType': 5,
                'codeSubject': 'ECM505',
                'weight': 1,
                'academicYear': 2022,
                'replaces': 1
            },
            {
                'id': 15,
                'idEvaluationType': 6,
                'codeSubject': 'ECM505',
                'weight': 1,
                'academicYear': 2022,
                'replaces': 2
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
                        if row['codeSubject'].upper() == codeSubject.upper()][0]
        except IndexError as error:
            return None

    async def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:

        subjects = [Subject(codeSubject=row['codeSubject'], name=row['name']) for row in self._professorSubjects
                    if row['idProfessor'] == idProfessor]
        return subjects if len(subjects) > 0 else None


    async def getCountStudentsByScore(self, gradeValue:float, codeSubject: str, idEvaluationType: int,
                                     academicYear: int) -> int:

        return len([row['idStudent'] for row in self._grades
                   if row['value'] == gradeValue
                   and row['codeSubject'].upper() == codeSubject.upper()
                   and row['academicYear'] == academicYear
                   and row['idEvaluationType'] == idEvaluationType])

    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> float:

        try:
            return [row['value'] for row in self._grades
                    if row['codeSubject'].upper() == codeSubject.upper()
                    and row['academicYear'] == academicYear
                    and row['idEvaluationType'] == idEvaluationType
                    and row['idStudent'] == idStudent][0]
        except IndexError as error:
            return None

    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:

        try:
            return [row['quantity'] for row in self._evalData
                    if row['codeSubject'].upper() == codeSubject.upper()
                    and row['academicYear'] == academicYear
                    and row['idEvaluationType'] == idEvaluationType][0]
        except IndexError:
            return 0

    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:

        try:
            return [row['quantity'] for row in self._evalWeight
                    if row['codeSubject'].upper() == codeSubject.upper()
                    and row['academicYear'] == academicYear
                    and row['idEvaluationType'] == idEvaluationType][0]
        except IndexError:
            return 0

    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:

        try:
            return [row['replaces'] for row in self._evalWeight
                    if row['codeSubject'].upper() == codeSubject.upper()
                    and row['academicYear'] == academicYear
                    and row['idEvaluationType'] == idEvaluationType][0]
        except IndexError:
            return 0


