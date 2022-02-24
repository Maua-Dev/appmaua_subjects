

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

                return query.scalars().all()
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')
        
    async def getSubjectsByCode(self,codeSubject: str) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                    where(SubjectDTO.codeSubject == codeSubject)
                )
                return query.scalars().first()
            except Exception as e:                              
                raise Exception(f'DataSource Error. {str(e)}')

    async def getSubjectStudents(self, codeSubject: str) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                    where(SubjectDTO.codeSubject == codeSubject)
                )

                return query.scalars.first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
        pass

    async def getAllSubjects(self) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO)
                )

                return query.scalars.all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
        pass

    async def getSubjectByProfessorId(self, idProfessor: int) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                    join(SubjectDTO.professors).
                    where(ProfessorSubjectDTO.idProfessor == idProfessor)
                )

                return query.scalars.all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getNumStudentsByGrades(self, gradeValue: float, codeSubject: str) -> SubjectDTO:
        return None