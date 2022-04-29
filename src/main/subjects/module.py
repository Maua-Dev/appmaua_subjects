

from typing import Any

from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.adapters.controllers.get_score_statistics_controller import GetScoreStatisticsController
from src.adapters.controllers.get_student_subject_scores_controller import GetStudentSubjectScoreController
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.adapters.controllers.get_student_course_average_controller import GetStudentCourseAverageController
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.domain.usecases.get_count_students_by_score_usecase import GetCountStudentsByScoreUsecase
from src.domain.usecases.get_count_students_by_course_and_year_usecase import GetCountStudentsByCourseAndYearUsecase
from src.domain.usecases.get_final_score_usecase import GetFinalScoreUsecase
from src.domain.usecases.get_student_course_id_usecase import GetStudentCourseIdUsecase
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.domain.usecases.get_subject_by_professor_id_usecase import GetSubjectByProfessorIdUsecase
from src.domain.usecases.get_student_subject_score_usecase import GetStudentSubjectScoreUsecase
from src.domain.usecases.get_subject_evaluation_quantity_usecase import GetSubjectEvaluationQuantityUsecase
from src.domain.usecases.get_subject_evaluation_weight_usecase import GetSubjectEvaluationWeightUsecase
from src.domain.usecases.get_course_name_by_student_id_usecase import GetCourseNameByStudentIdUsecase
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
            SubjectRepositoryMock if Envs.IsMock() else SubjectRepositoryImp,
            PostgresDataSource,
            GetScoreStatisticsController,
            GetCountStudentsByScoreUsecase,
            GetStudentSubjectScoreUsecase,
            GetStudentSubjectScoreController,
            GetFinalScoreUsecase,
            GetSubjectEvaluationQuantityUsecase,
            GetSubjectEvaluationWeightUsecase,
            GetCountStudentsByCourseAndYearUsecase,
            GetStudentCourseIdUsecase,
            GetStudentCourseYearUsecase,
            GetCourseNameByStudentIdUsecase,
            GetStudentCourseAverageController

        ]




    
        
