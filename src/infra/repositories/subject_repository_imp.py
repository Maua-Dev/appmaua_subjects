from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.infra.datasources.datasource_interface import IDataSource


class SubjectRepositoryImp(ISubjectRepository):
    def __init__(self,datasource: IDataSource) -> None:
        super().__init__()
        self._datasource = datasource
    
    def getStudentSubjects(self, idStudent: int) -> tuple:
        try:
            response = self._datasource.getSubjectsByStudent(idStudent=idStudent)    
            return list(map(lambda x: x.toEntity(),response))
        except Exception as error:                
            raise error

    def getSubjectStudents(self, codeSubject: str) -> tuple:
        pass

    def getAllSubjects(self) -> tuple:
        pass

    def getSubjectByCode(self, codeSubject: str) -> tuple:
        pass

    def getSubjectByProfessorId(self, idProfessor: int) -> tuple:
        pass