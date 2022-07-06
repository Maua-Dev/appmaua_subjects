from decimal import Decimal

from src.domain.entities.grade import Grade
from src.domain.entities.professor import Professor
from src.domain.entities.subject import Subject
from src.domain.enums.degree_enum import DegreeEnum
from src.domain.enums.evaluation_type import EVALUATION_TYPE
from src.domain.enums.semester import SEMESTER
from src.domain.enums.situation import SITUATION
from src.domain.enums.year import YEAR
from src.infra.dtos.subject_dynamo_dto import SubjectDynamoDTO


class Test_SubjectDynamoDTO:

    def test_dynamo_to_entity(self):
        data = {
            'grades': [
                    {'evaluationType': 'P1', 'value': Decimal('4.8'), 'weight': Decimal('0.3')},
                    {'evaluationType': 'P2', 'value': Decimal('3.5'), 'weight': Decimal('0.3')},
                    {'evaluationType': 'T1', 'value': Decimal('2.7'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T2', 'value': Decimal('9.1'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T3', 'value': Decimal('5.3'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T4', 'value': Decimal('9.9'), 'weight': Decimal('0.1')}],
            'degreeCode': 'ECM',
            'professor': {'name': 'Murilo Carvalho', 'email': 'murilocarvalho@maua.br', 'tel': '11940028922'},
            'coordinator': {'name': 'Murilo Carvalho', 'email': 'murilocarvalho@maua.br', 'tel': '11940028922'},
            'start_time': Decimal('34228000'),
            'end_time': Decimal('40228000'),
            'subjectName': 'Desenvolvimento de Aplicativos Híbridos',
            'subjectCode': 'ECM963',
            'day_of_week': Decimal('5'),
            'haveMultipleClasses': False,
            'situation': 'IN_PROGRESS',
            'year': Decimal('2022'),
            'studentRA': '17.00163-3',
            'academicYear': Decimal('5'),
            'semester': 'AN'}

        subject = SubjectDynamoDTO.fromDynamo(data)

        expected = Subject(
            name="Desenvolvimento de Aplicativos Híbridos",
            code="ECM963",
            year="2022",
            academicYear=YEAR._5,
            degreeCode=DegreeEnum.ECM,
            semester=SEMESTER(SEMESTER.AN),
            situation=SITUATION.IN_PROGRESS,
            grades=[
                Grade(evaluationType=EVALUATION_TYPE.P1, value=Decimal('4.8'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.P2, value=Decimal('3.5'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.T1, value=Decimal('2.7'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T2, value=Decimal('9.1'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T3, value=Decimal('5.3'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T4, value=Decimal('9.9'), weight=Decimal('0.1'))

            ],
            professor=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922'),
            coordinator=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922')
            )

        assert subject.toEntity() == expected


    def test_entity_to_entity(self):

        subject = Subject(
            name="Desenvolvimento de Aplicativos Híbridos",
            code="ECM963",
            year="2022",
            academicYear=YEAR._5,
            degreeCode=DegreeEnum.ECM,
            semester=SEMESTER(SEMESTER.AN),
            situation=SITUATION.IN_PROGRESS,
            grades=[
                Grade(evaluationType=EVALUATION_TYPE.P1, value=Decimal('4.8'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.P2, value=Decimal('3.5'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.T1, value=Decimal('2.7'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T2, value=Decimal('9.1'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T3, value=Decimal('5.3'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T4, value=Decimal('9.9'), weight=Decimal('0.1'))

            ],
            professor=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922'),
            coordinator=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922')
        )

        data = SubjectDynamoDTO.fromEntity(subject)

        parsedSubject = data.toEntity()

        assert subject == parsedSubject


    def test_entity_to_dynamo(self):
        expected = {
            'grades': [
                    {'evaluationType': 'P1', 'value': Decimal('4.8'), 'weight': Decimal('0.3')},
                    {'evaluationType': 'P2', 'value': Decimal('3.5'), 'weight': Decimal('0.3')},
                    {'evaluationType': 'T1', 'value': Decimal('2.7'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T2', 'value': Decimal('9.1'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T3', 'value': Decimal('5.3'), 'weight': Decimal('0.1')},
                    {'evaluationType': 'T4', 'value': Decimal('9.9'), 'weight': Decimal('0.1')}],
            'degreeCode': 'ECM',
            'professor': {'name': 'Murilo Carvalho', 'email': 'murilocarvalho@maua.br', 'tel': '11940028922'},
            'coordinator': {'name': 'Murilo Carvalho', 'email': 'murilocarvalho@maua.br', 'tel': '11940028922'},
            'subjectName': 'Desenvolvimento de Aplicativos Híbridos',
            'subjectCode': 'ECM963',
            'situation': 'IN_PROGRESS',
            'year': Decimal('2022'),
            'studentRA': '17.00163-3',
            'academicYear': Decimal('5'),
            'semester': 'AN'}



        entity = Subject(
            name="Desenvolvimento de Aplicativos Híbridos",
            code="ECM963",
            year="2022",
            academicYear=YEAR._5,
            degreeCode=DegreeEnum.ECM,
            semester=SEMESTER(SEMESTER.AN),
            situation=SITUATION.IN_PROGRESS,
            grades=[
                Grade(evaluationType=EVALUATION_TYPE.P1, value=Decimal('4.8'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.P2, value=Decimal('3.5'), weight=Decimal('0.3')),
                Grade(evaluationType=EVALUATION_TYPE.T1, value=Decimal('2.7'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T2, value=Decimal('9.1'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T3, value=Decimal('5.3'), weight=Decimal('0.1')),
                Grade(evaluationType=EVALUATION_TYPE.T4, value=Decimal('9.9'), weight=Decimal('0.1'))

            ],
            professor=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922'),
            coordinator=Professor(name="Murilo Carvalho", email="murilocarvalho@maua.br", phoneNumber='11940028922')
            )

        subjectDto = SubjectDynamoDTO.fromEntity(entity)

        parsedSubject = subjectDto.toDynamo(studentRA='17.00163-3')

        assert parsedSubject == expected


