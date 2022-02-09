

from typing import List
from src.external.postgres.db_config import DBConnectionHandler
from src.infra.datasources.datasource_interface import IDataSource
from src.infra.dtos.Subject import StudentSubjectDTO,SubjectDTO



class PostgresDataSource(IDataSource):

    def getSubjectsByStudent(self, idStudent: int) -> List[SubjectDTO]:
        with DBConnectionHandler() as db:
            try:                
                subjects = db.session.query(SubjectDTO).join('students').filter(StudentSubjectDTO.idStudent == idStudent).all()                
                return subjects
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')
        
    def getSubjectsByCode(self,codeSubject: str) -> SubjectDTO:
        with DBConnectionHandler() as db:
            try:                
                subjects = db.session.query(SubjectDTO).filter(SubjectDTO.codeSubject == codeSubject).first()
                return subjects
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')

    def getSubjectStudents(self, codeSubject: str) -> List[int]:
        pass

    def getAllSubjects(self) -> SubjectDTO:
        with DBConnectionHandler() as db:
            try:
                subjects = db.session.query(SubjectDTO).all()
                return subjects
            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
        pass

    def getSubjectByProfessorId(self, idProfessor: int) -> SubjectDTO:
        pass