import pytest
from src.domain.entities.student import Student
from src.domain.errors.errors import EntityError


class Test_Student():

    def test_create_valid_student(self):
        student = Student(name='Joao do teste', idDegree=1, idSubjects=[1,2,3,4,5])
        assert len(student.name) > 0
        assert student.name == 'Joao Do Teste'
        assert len(student.idSubjects) > 0
        assert len(student.idSubjects) == 5
        assert student.idDegree == 1

    def test_create_invalid_student1(self):
        with pytest.raises(EntityError):
            Student(name='', idDegree=1, idSubjects=[1,2,3,4,5])

    def test_create_invalid_student2(self):
        with pytest.raises(EntityError):
            Student(name='Joao do teste', idDegree=0, idSubjects=[1,2,3,4,5])

    def test_create_invalid_student3(self):
        with pytest.raises(EntityError):
            Student(name='Joao do teste', idDegree=1, idSubjects=[])