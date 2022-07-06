import decimal
from decimal import Decimal


from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR


class SubjectDynamoDTO:
    name: str
    code: str
    year: int
    academicYear: int
    degreeCode: str
    semester: str
    situation: str
    grades: list[dict]
    professor: dict
    coordinator: dict
    studentRA: str

    @staticmethod
    def parseNumber(number: (int, float), decimals: int) -> Decimal:
        """
        Parse a number to a Decimal with a certain number of decimals.
        :param number: The number to parse.
        :param decimals: The number of decimals (ex: 2 would make "0.01").
        """
        if decimals == 0:
            return Decimal(number).quantize(Decimal(f'1'), rounding=decimal.ROUND_HALF_UP)
        elif decimals < 0:
            raise ValueError("decimals must be greater than 0")

        return Decimal(number).quantize(Decimal(f'0.{ "0" * (decimals - 1 ) }1'), rounding=decimal.ROUND_HALF_UP)


    @staticmethod
    def fromDynamo(data: dict):
        grades = []
        for g in data.get("grades"):
            grades.append(dict(evaluationType=str(g["evaluationType"]),
                               value=float(g["value"]),
                               weight=float(g["weight"]) if g.get("weight") else None)
            )

        professor = dict(
            name=data.get("professor").get("name"),
            email=data.get("professor").get("email"),
            phoneNumber=data.get("professor").get("tel")
        )

        coordinator = dict(
            name=data.get("coordinator").get("name"),
            email=data.get("coordinator").get("email"),
            phoneNumber=data.get("coordinator").get("tel")
        )

        return SubjectDynamoDTO(
            name=data.get("subjectName"),
            code=data.get("subjectCode"),
            year=data.get("year"),
            academicYear=data.get("academicYear"),
            degreeCode=data.get("degreeCode"),
            semester=data.get("semester"),
            situation=data.get("situation"),
            grades=grades,
            professor=professor,
            coordinator=coordinator
        )


    @staticmethod
    def fromEntity(entity: Subject):

        return SubjectDynamoDTO(
            name=str(entity.name),
            code=str(entity.code),
            year=int(entity.year),
            academicYear=int(entity.academicYear.value),
            degreeCode=str(entity.degreeCode.name),
            semester=str(entity.semester.name),
            situation=str(entity.situation.name),
            grades=[ dict(
                evaluationType=g.evaluationType.value,
                value=g.value,
                weight=g.weight
            ) for g in entity.grades ],
            professor=entity.professor.dict(),
            coordinator=entity.coordinator.dict()
        )


    def __init__(self, **kwargs) -> None:
        self.name = str(kwargs.get("name"))
        self.code = str(kwargs.get("code"))
        self.year = int(kwargs.get("year"))
        self.academicYear = int(kwargs.get("academicYear"))
        self.degreeCode = str(kwargs.get("degreeCode"))
        self.semester = str(kwargs.get("semester"))
        self.situation = str(kwargs.get("situation"))
        self.grades = kwargs.get("grades")
        self.professor = kwargs.get("professor")
        self.coordinator = kwargs.get("coordinator")


    def toEntity(self) -> Subject:
        # convert Grades
        gradesParsed = []
        for grade in self.grades:
            evaluationType = EVALUATION_TYPE[grade.get("evaluationType")]
            value = float(grade.get("value")) if grade.get("value") else None
            weight = float(grade.get("weight"))
            gradesParsed.append(Grade(evaluationType=evaluationType, value=value, weight=weight))

        # convert Professor
        professorParsed = Professor(name=self.professor.get("name"),
                              email=self.professor.get("email"),
                              phoneNumber=self.professor.get("phoneNumber"))

        # convert Coordinator
        coordinatorParsed = Professor(name=self.coordinator.get("name"),
                                email=self.coordinator.get("email"),
                                phoneNumber=self.coordinator.get("phoneNumber"))

        return Subject(
            name=self.name,
            code=self.code,
            year=self.year,
            academicYear=YEAR[f"_{self.academicYear}"],
            degreeCode=DegreeEnum[self.degreeCode],
            semester=SEMESTER[self.semester],
            situation=SITUATION[self.situation],
            grades=gradesParsed,
            professor=professorParsed,
            coordinator=coordinatorParsed,
        )


    def toDynamo(self, studentRA: str) -> dict:
        # convert Grades
        gradesParsed = []
        for g in self.grades:
            gradesParsed.append(dict(
                evaluationType=g.get("evaluationType"),
                value=SubjectDynamoDTO.parseNumber(number=g.get("value"), decimals=1),
                weight=SubjectDynamoDTO.parseNumber(number=g.get("weight"), decimals=1) if g.get("weight") else None
            ))

        # convert Professor
        professorParsed = dict(
            name=self.professor.get("name"),
            email=self.professor.get("email"),
            tel=self.professor.get("phoneNumber")
        )

        # convert Coordinator
        coordinatorParsed = dict(
            name=self.coordinator.get("name"),
            email=self.coordinator.get("email"),
            tel=self.coordinator.get("phoneNumber")
        )

        return dict(
            subjectName=self.name,
            subjectCode=self.code,
            studentRA=studentRA,
            year=SubjectDynamoDTO.parseNumber(number=self.year, decimals=0),
            academicYear=SubjectDynamoDTO.parseNumber(number=self.academicYear, decimals=0),
            degreeCode=self.degreeCode,
            semester=self.semester,
            situation=self.situation,
            grades=gradesParsed,
            professor=professorParsed,
            coordinator=coordinatorParsed
        )



