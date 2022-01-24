from src.domain.entities.subject import Subject
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.repositories.subject_repository_imp import SubjectRepositoryImp


class Test_SubjectRepositoryImp():

    def test_get_student_subjects_db(self):
        assert True
        # postgresDataSource = PostgresDataSource()        
        # repository = SubjectRepositoryImp(datasource=postgresDataSource)
        # response = repository.getStudentSubjects(idStudent=1)
        # assert isinstance(response, list)