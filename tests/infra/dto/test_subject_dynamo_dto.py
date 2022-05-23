from src.domain.entities.course import Course
from src.domain.entities.degree import Degree
from src.domain.entities.score import Score
from src.domain.entities.student import Student
from src.domain.entities.subject import Subject
from src.domain.enums.evaluation_type import EvaluationType
from src.infra.dtos.subject_dynamo_dto import SubjectDynamoDTO


class Test_SubjectDynamoDTO():
    courseMock = Course(codeCourse="ECM", name="Engenharia de Computação")
    degreeMock = Degree(name="Engenharia de Computação", duration=5, codeDegree="ECM", subjects=["ECM256"])
    scoreMock = Score(value=10, academicYear=2020, evaluationType=EvaluationType.P1, weight=3.0)
    studentMock = Student(name="Bruno Vilardi", codeStudent="19002231", codeDegree="ECM", subjects=["ECM256"], ra="19002231")
    subjectMock = Subject(codeSubject="ECM256", name="Redes de Computadores")

    def test_to_entity(self):
        subjectDTO = SubjectDynamoDTO(
            subjectCode="ECM256",
            subjectName="Redes de Computadores",
            courseCode="ECM",
            courseName="Engenharia de Computação",
            degreeName="Engenharia de Computação",
            degreeDuration=5,
            degreeCode="ECM",
            degreeSubjects=["ECM256"],
            studentName="Bruno Vilardi",
            studentCode="19002231",
            studentCodeDegree="ECM",
            studentSubjects=["ECM256"],
            scoreValue=10,
            scoreAcademicYear=2020,
            scoreEvaluationType=EvaluationType.P1,
            scoreWeight=3.0
        )
        entity = subjectDTO.toEntity()
        assert entity["Subject"] == self.subjectMock
        assert entity["Course"] == self.courseMock
        assert entity["Degree"] == self.degreeMock
        assert entity["Student"] == self.studentMock
        assert entity["Score"] == self.scoreMock

    def test_from_entity(self):
        dto = SubjectDynamoDTO()
        dto.appendEntity(self.subjectMock)
        dto.appendEntity(self.courseMock)
        dto.appendEntity(self.degreeMock)
        dto.appendEntity(self.studentMock)
        dto.appendEntity(self.scoreMock)

        assert dto.subjectCode == "ECM256"
        assert dto.subjectName == "Redes de Computadores"
        assert dto.courseCode == "ECM"
        assert dto.courseName == "Engenharia de Computação"
        assert dto.degreeName == "Engenharia de Computação"
        assert dto.degreeDuration == 5
        assert dto.degreeCode == "ECM"
        assert dto.degreeSubjects == ["ECM256"]
        assert dto.studentName == "Bruno Vilardi"
        assert dto.studentCodeDegree == "ECM"
        assert dto.studentCode == "19002231"
        assert dto.studentSubjects == ["ECM256"]
        assert dto.scoreValue == 10
        assert dto.scoreAcademicYear == 2020
        assert dto.scoreEvaluationType == EvaluationType.P1
        assert dto.scoreWeight == 3.0

    def test_from_entity_to_entity(self):
        a = SubjectDynamoDTO()
        a.appendEntity(self.subjectMock)
        a.appendEntity(self.courseMock)
        a.appendEntity(self.degreeMock)
        a.appendEntity(self.studentMock)
        a.appendEntity(self.scoreMock)

        res = a.toEntity()

        assert res["Student"] == self.studentMock
        assert res["Score"] == self.scoreMock
        assert res["Subject"] == self.subjectMock
        assert res["Course"] == self.courseMock
        assert res["Degree"] == self.degreeMock

    def test_to_dynamo(self):

        expected = {
        "subjectCode": "ECM256",
        "subjectName": "Redes de Computadores",
        "courseCode": "ECM",
        "courseName": "Engenharia de Computação",
        "degreeName": "Engenharia de Computação",
        "degreeDuration": 5,
        "degreeCode": "ECM",
        "degreeSubjects": ["ECM256"],
        "studentName": "Bruno Vilardi",
        "studentCodeDegree": "ECM",
        "studentCode": "19002231",
        "studentSubjects": ["ECM256"],
        "scoreValue": 10,
        "scoreAcademicYear": 2020,
        "scoreEvaluationType": EvaluationType.P1,
        "scoreWeight": 3.0
        }

        subjectDTO = SubjectDynamoDTO()
        subjectDTO.appendEntity(self.subjectMock)
        subjectDTO.appendEntity(self.courseMock)
        subjectDTO.appendEntity(self.degreeMock)
        subjectDTO.appendEntity(self.studentMock)
        subjectDTO.appendEntity(self.scoreMock)

        res = subjectDTO.toDynamo()

        assert res == expected
