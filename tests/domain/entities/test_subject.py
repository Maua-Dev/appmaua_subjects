import pytest
from src.domain.entities.subject import Subject
from src.domain.errors.errors import EntityError
class Test_Subject():
    def test_create_valid_subject(self):
        subject = Subject(id=1,codeSubject='ECM400',name='Engenharia de Software')
        assert len(subject.codeSubject) > 0
        assert len(subject.name) > 0
    def test_create_invalid_subject(self):        
        with pytest.raises(EntityError):
            Subject(id=1,codeSubject='',name='')
        