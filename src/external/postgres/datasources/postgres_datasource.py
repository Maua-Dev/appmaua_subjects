

from typing import List

from sqlalchemy.future import select
from src.external.postgres.db_config_async import AsyncDBConnectionHandler
from src.infra.datasources.datasource_interface import IDataSource
from src.infra.dtos.Subject import StudentSubjectDTO,SubjectDTO



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
        
