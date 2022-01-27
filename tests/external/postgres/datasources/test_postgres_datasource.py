import pytest
from src.envs import EnvEnum, Envs
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.dtos.Subject.subject_dto import SubjectDTO


class Test_PostgresDataSource:
    @pytest.mark.asyncio
    async def test_query_with_no_error(self):        
        Envs.appEnv = EnvEnum.LOCAL
        postgresDataSource = PostgresDataSource()
        response = await postgresDataSource.getSubjectsByStudent(idStudent=1)
        assert isinstance(response, list)
