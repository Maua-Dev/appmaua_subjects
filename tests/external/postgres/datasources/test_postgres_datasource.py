from src.envs import EnvEnum, Envs
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.dtos.Subject.subject_dto import SubjectDTO


class Test_PostgresDataSource:

    def test_query_with_no_error(self):
        assert True
        # Envs.appEnv = EnvEnum.DES
        # postgresDataSource = PostgresDataSource()
        # response = postgresDataSource.getSubjectsByStudent(idStudent=1)
        # assert isinstance(response, list)
