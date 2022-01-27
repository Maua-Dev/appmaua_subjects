from typing import List
from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.infra.datasources.datasource_interface import IDataSource


class SubjectRepositoryImp(ISubjectRepository):
    def __init__(self,datasource: IDataSource) -> None:
        super().__init__()
        self._datasource = datasource
    
    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        try:
            response = await self._datasource.getSubjectsByStudent(idStudent=idStudent)    
            return list(map(lambda x: x.toEntity(),response))
        except Exception as error:                
            raise error