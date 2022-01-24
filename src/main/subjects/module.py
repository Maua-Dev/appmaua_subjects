

from typing import Any
from src.adpters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.domain.usecases.get_student_subjects_score_usecase import GetStudentSubjectsScoreUsecase
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.external.postgres.datasources.postgres_datasource import PostgresDataSource
from src.infra.repositories.subject_repository_imp import SubjectRepositoryImp

class Modular:
    
    @staticmethod
    def getInject(args: Any):
        for i in Module.binds:
            if( i == args or issubclass(i,args)):
                try:
                    inject = (args if i == args  else i).__init__.__annotations__
                except AttributeError:
                    return i()

                if len(inject) <= 1 :
                    return i()
                else:   
                    params = {}
                    for j in range(0,len(inject)-1):
                        instance = Modular.getInject(list(inject.values())[j])
                        param = list(inject.keys())[j]
                        params[param] = instance
                    return i(**params)
        return None;



class Module:
    binds = [
        GetStudentSubjectsController,
        GetStudentSubjectsUsecase,
        GetStudentSubjectsScoreUsecase,
        SubjectRepositoryImp,
        PostgresDataSource
    ]




    
        
