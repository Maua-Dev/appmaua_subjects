

from typing import List

from sqlalchemy.future import select
from src.external.postgres.db_config_async import AsyncDBConnectionHandler
from src.infra.datasources.datasource_interface import IDataSource
from src.infra.dtos.Subject import StudentSubjectDTO, SubjectDTO, ProfessorSubjectDTO


class PostgresDataSource(IDataSource):

    async def getSubjectsByStudent(self, idStudent: int) -> List[SubjectDTO]:
        async with AsyncDBConnectionHandler().session() as s:
            try:             
                query = await s.execute(
                    select(SubjectDTO).
                    join(SubjectDTO.students).
                    where(StudentSubjectDTO.idStudent == idStudent)
                )   
                # subjects = db.session.query(SubjectDTO).join('students').filter(StudentSubjectDTO.idStudent == idStudent).all()                
                return query.scalars().all()
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')
        
    async def getSubjectsByCode(self,codeSubject: str) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:                
                # subjects = db.session.query(SubjectDTO).filter(SubjectDTO.codeSubject == codeSubject).first()
                query = await s.execute(
                    select(SubjectDTO).
                    where(SubjectDTO.codeSubject == codeSubject)
                )
                return query.scalars().first()
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')

    def getSubjectStudents(self, codeSubject: str) -> SubjectDTO:
        with DBConnectionHandler() as db:
            try:
                subjects = db.session.query(SubjectDTO).filter(SubjectDTO.codeSubject == codeSubject).first()
                return subjects
            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
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
        with DBConnectionHandler() as db:
            try:
                subjects = db.session.query(SubjectDTO).join('professors').filter(ProfessorSubjectDTO.idProfessor == idProfessor).all()
                return subjects
            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')