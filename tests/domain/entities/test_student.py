import pytest

from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.entities.student import Student
from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.domain.enums.period import PERIOD
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR
from src.helpers.errors.domain_errors import EntityError


class Test_student:
    def test_student(self):
        student = Student(
                    name="Bruno Vilardi",
                    ra="19003315",
                    email="bruno@bruno.com",
                    password="Teste123!",
                    degreeCode=DegreeEnum.ECM,
                    academicYear=YEAR._4,
                    subjects=[Subject(
                        name="Banco de Dados",
                        code="ECM401",
                        degreeCode=DegreeEnum.ECM,
                        year=2022,
                        academicYear=YEAR._4,
                        semester=SEMESTER.AN,
                        situation=SITUATION.IN_PROGRESS,
                        grades=[
                            Grade(
                                value=3.0,
                                evaluationType=EVALUATION_TYPE.P1,
                                weight=0.2,
                            ),
                            Grade(
                                value=None,
                                evaluationType=EVALUATION_TYPE.P2,
                                weight=0.4,
                            ),
                            Grade(
                                value=None,
                                evaluationType=EVALUATION_TYPE.T1,
                                weight=0.1
                            ),
                            Grade(
                                value=None,
                                evaluationType=EVALUATION_TYPE.T2,
                                weight=0.1
                            ),
                            Grade(
                                value=None,
                                evaluationType=EVALUATION_TYPE.T3,
                                weight=0.1
                            ),
                            Grade(
                                value=None,
                                evaluationType=EVALUATION_TYPE.T4,
                                weight=0.1
                            )
                        ],
                        professor=Professor(
                            name="Aparecido Valdemir de Freitas",
                            email="aparecido.freitas@maua.br",
                            phoneNumber="4239-3009"
                        ),
                        coordinator=Professor(
                            name="Angelo Sebastiao Zanini",
                            email="angelo.zanini@maua.br",
                            phoneNumber="4239-3009"
                        )
                    )],
                    period=PERIOD.DAY,
                    photo="https://drive.google.com/uc?export=view&id=1IKIyM5G5jivSx0y7YLnZ-XWD-QvnQ5AC"

        )
        assert type(student) == Student
        assert student.name == "Bruno Vilardi"

    async def test_student_entity_error(self):
        with pytest.raises(EntityError):
            await Student(name='')