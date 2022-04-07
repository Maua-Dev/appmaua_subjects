from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.adapters.viewmodels.average_subjects_viewmodel import AverageSubjectsViewModel, AverageViewModel
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
from src.domain.usecases.get_course_name_by_student_id_usecase import GetCourseNameByStudentIdUsecase
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
from src.domain.usecases.get_final_score_usecase import GetFinalScoreUsecase

from src.adapters.helpers.http_models import *


class GetStudentCourseAverageController:
    def __init__(self,
        getStudentCourseYearUsecase: GetStudentCourseYearUsecase,
        getCourseNameByStudentIdUsecase: GetCourseNameByStudentIdUsecase,
        getStudentSubjectsUsecase: GetStudentSubjectsUsecase,
        getFinalScoreUsecase: GetFinalScoreUsecase
        ) -> None:
        
        self._getStudentCourseYearUsecase = getStudentCourseYearUsecase
        self._getCourseNameByStudentIdUsecase = getCourseNameByStudentIdUsecase
        self._getStudentSubjectsUsecase = getStudentSubjectsUsecase
        self._getFinalScoreUsecase = getFinalScoreUsecase

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['idStudent'] is None:
                return BadRequest(f"idStudent is invalid.")

            if req.query['academicYear'] is None:
                return BadRequest(f"academicYear is invalid. (academicYear = None)")

            idStudent = req.query['idStudent']
            academicYear = req.query['academicYear']

            ano = await self._getStudentCourseYearUsecase(idStudent=idStudent)
            nomeGraduacao = await self._getCourseNameByStudentIdUsecase(idStudent=idStudent)

            medias = []
            
            listSubjects = await self._getStudentSubjectsUsecase(idStudent=idStudent)
            for subject in listSubjects:
                media, partialScore = await self._getFinalScoreUsecase(
                    codeSubject=subject.codeSubject,
                    academicYear=academicYear,
                    idStudent=idStudent
                )
                medias.append(AverageViewModel(
                    materia=subject.name,
                    media=media))

            return Ok(AverageSubjectsViewModel(nomeGraduacao=nomeGraduacao,
                                    ano=ano,
                                    medias=medias,
                                    isPartialScore=partialScore))

        except NoItemsFound as e:
            return NotFound('(GetStudentCourseAverageController) No course found -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)