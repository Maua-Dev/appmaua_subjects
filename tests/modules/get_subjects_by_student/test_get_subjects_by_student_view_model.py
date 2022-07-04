import pytest

from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR
from src.modules.get_subjects_by_student.get_subjects_by_student_viewmodel import GetSubjectsByStudentViewmodel


class Test_GetSubjectByStudentViewModel:
    @pytest.mark.asyncio
    async def test_get_subject_by_student_view_model(self):
        subjects = [
            Subject(
                name="Engenharia de Software",
                code="ECM231",
                degreeCode=DegreeEnum.ECM,
                year=2022,
                academicYear=YEAR._4,
                semester=SEMESTER.AN,
                situation=SITUATION.IN_PROGRESS,
                grades=[
                    Grade(
                        value= 8.5,
                        evaluationType= EVALUATION_TYPE.P1,
                        weight= 0.1,
                    ),
                    Grade(
                        value=4.0,
                        evaluationType=EVALUATION_TYPE.P2,
                        weight=0.1,
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.P3,
                        weight=0.2
                    ),
                    Grade(
                        value=None,
                        evaluationType=EVALUATION_TYPE.P4,
                        weight=0.2
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
                    name="Ana Paula Gonçalves Serra",
                    email="ana.serra@maua.br",
                    phoneNumber="4239-3008"),
                coordinator=Professor(
                    name="Angelo Sebastiao Zanini",
                    email="angelo.zanini@maua.br",
                    phoneNumber="4239-3009"
                )
            ),
            Subject(
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
            )
        ]
        subjectsViewModel = GetSubjectsByStudentViewmodel(subjects).to_dict()
        result = [{'name': 'Engenharia de Software',
                   'code': 'ECM231',
                   'grades': [{'value': 8.5,'evaluationType': 'P1','weight': 0.1},
                              {'value': 4.0,'evaluationType': 'P2','weight': 0.1},
                              {'value': None, 'evaluationType': 'P3', 'weight': 0.2},
                              {'value': None, 'evaluationType': 'P4', 'weight': 0.2},
                              {'value': None, 'evaluationType': 'T1', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T2', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T3', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T4', 'weight': 0.1}]},
                  {'name': 'Banco de Dados',
                   'code': 'ECM401',
                   'grades': [{'value': 3.0, 'evaluationType': 'P1', 'weight': 0.2},
                              {'value': None, 'evaluationType': 'P2', 'weight': 0.4},
                              {'value': None, 'evaluationType': 'T1', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T2', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T3', 'weight': 0.1},
                              {'value': None, 'evaluationType': 'T4', 'weight': 0.1}]
                   }]

        assert subjectsViewModel == result
