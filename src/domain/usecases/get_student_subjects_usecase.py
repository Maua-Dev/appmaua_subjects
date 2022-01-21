from typing import List
from src.domain.errors.errors import UnexpectedError
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.entities.subject import Subject
class GetStudentSubjectsUsecase:
    def __init__(self,subjectRepository: ISubjectRepository) -> None:
        self._subjectRepository = subjectRepository
    
    def __call__(self,idStudent: int) -> List[Subject]:
        try:
            if(idStudent == None): raise Exception()
            subjects = self._subjectRepository.getStudentSubjects(idStudent=idStudent)

            return subjects;

        except:
            raise UnexpectedError('GetStudentSubject')