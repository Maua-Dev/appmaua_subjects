import pytest
from src.domain.entities.student import Student
from src.domain.errors.errors import EntityError


class Test_Student():

    def test_create_valid_student(self):
        student = Student(name='Joao do teste', codeDegree="ENGCOMP", subjects=['ECM505', 'ECM501'], ra='123456789')
        assert len(student.name) > 0
        assert student.name == 'Joao Do Teste'
        assert len(student.subjects) > 0
        assert len(student.subjects) == 2
        assert student.codeDegree == "ENGCOMP"

    def test_create_invalid_student1(self):
        with pytest.raises(EntityError):
            Student(name='', codeDegree="ENGCOMP", subjects=['ECM505', 'ECM501'], ra='123456789')

    def test_create_invalid_student2(self):
        with pytest.raises(EntityError):
            Student(name='Joao do teste', codeDegree="", subjects=['ECM505', 'ECM501'], ra='123456789')

    def test_create_invalid_student3(self):
        with pytest.raises(EntityError):
            Student(name='Joao do teste', codeDegree="ENGCOMP", subjects=[''], ra='123456789')