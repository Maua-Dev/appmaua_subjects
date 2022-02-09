from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.infra.datasources.datasource_interface import IDataSource
from typing import List


class SubjectRepositoryImp(ISubjectRepository):
    def __init__(self,datasource: IDataSource) -> None:
        super().__init__()
        self._datasource = datasource
    
    def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        try:
            response = self._datasource.getSubjectsByStudent(idStudent=idStudent)    
            return list(map(lambda x: x.toEntity(),response))
        except Exception as error:                
            raise error

    def getSubjectStudents(self, codeSubject: str) -> List[int]:
        pass

    def getAllSubjects(self) -> List[Subject]:
        pass

    def getSubjectByCode(self, codeSubject: str) -> Subject:
        try:
            respose = self._datasource.getSubjectsByCode(codeSubject=codeSubject)
            return respose.toEntity()
        except Exception as error:                
            raise error

    def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:
        pass