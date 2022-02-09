

from typing import Any

from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.domain.usecases.get_student_subjects_score_usecase import GetStudentSubjectsScoreUsecase
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.domain.usecases.get_subject_by_professor_id_usecase import GetSubjectByProfessorIdUsecase
from src.envs import Envs
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.repositories.subject_repository_imp import SubjectRepositoryImp
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock


class Modular:   
    @staticmethod
    def getInject(args: Any):
        for i in Module.getBinds():
            if(i == args or issubclass(i, args)):
                try:
                    inject = (args if i == args else i).__init__.__annotations__
                except AttributeError:
                    return i()

                if len(inject) <= 1:
                    return i()
                else:   
                    params = {}
                    for j in range(0, len(inject)-1):
                        instance = Modular.getInject(list(inject.values())[j])
                        param = list(inject.keys())[j]
                        params[param] = instance
                    return i(**params)
        return None;



class Module:
    
    @staticmethod
    def getBinds():
        return [
        GetSubjectByProfessorIdController,
        GetSubjectByProfessorIdUsecase,
        GetSubjectByCodeUsecase,
        GetSubjectByCodeController,
        GetAllSubjectsController,
        GetAllSubjectsUsecase,
        GetStudentSubjectsController,
        GetStudentSubjectsUsecase,
        GetStudentSubjectsScoreUsecase,
        SubjectRepositoryMock if Envs.IsMock() else SubjectRepositoryImp,        
        PostgresDataSource
    ]




    
        
