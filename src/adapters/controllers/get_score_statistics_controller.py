from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.usecases.get_count_students_by_score_usecase import GetCountStudentsByScoreUsecase
from src.domain.usecases.get_count_students_by_course_and_year_usecase import GetCountStudentsByCourseAndYearUsecase
from src.domain.usecases.get_student_course_id_usecase import GetStudentCourseIdUsecase
from src.domain.usecases.get_student_course_year_usecase import GetStudentCourseYearUsecase
from src.adapters.helpers.http_models import *
from src.adapters.viewmodels.bar_chart import *


class GetScoreStatisticsController:
    def __init__(self, getCountStudentsByScoreUsecase: GetCountStudentsByScoreUsecase,
                 getCountStudentsByCourseAndYearUsecase: GetCountStudentsByCourseAndYearUsecase,
                 getStudentCourseIdUsecase: GetStudentCourseIdUsecase,
                 getStudentCourseYearUsecase: GetStudentCourseYearUsecase) -> None:

        self._getCountStudentsByScoreUsecase = getCountStudentsByScoreUsecase
        self._getCountStudentsByCourseAndYearUsecase = getCountStudentsByCourseAndYearUsecase
        self._getStudentCourseIdUsecase = getStudentCourseIdUsecase
        self._getStudentCourseYearUsecase = getStudentCourseYearUsecase

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['codeSubject'] is None :
                return BadRequest(f"codeSubject is invalid. (codeSubject = None)")

            if req.query['idEvaluationType'] is None:
                return BadRequest(f"idEvaluationType is invalid. (idEvaluationType = None)")

            if req.query['academicYear'] is None:
                return BadRequest(f"academicYear is invalid. (academicYear = None)")

            if req.query['idStudent'] is None:
                return BadRequest(f"idStudent is invalid. (idStudent = None)")

            codeSubject = req.query['codeSubject']
            idEvaluationType = req.query['idEvaluationType']
            academicYear = req.query['academicYear']
            idStudent = req.query['idStudent']

            courseId = await self._getStudentCourseIdUsecase(idStudent, academicYear)
            courseYear = await self._getStudentCourseYearUsecase(idStudent, academicYear)
            courseCount = await self._getCountStudentsByCourseAndYearUsecase(courseId, courseYear, academicYear)

            bars = [GraphBar(score=-2, studentCount=await self._getCountStudentsByScoreUsecase(-2, codeSubject,
                                                                                               idEvaluationType,
                                                                                               academicYear)),
                    GraphBar(score=-1, studentCount=await self._getCountStudentsByScoreUsecase(-1, codeSubject,
                                                                                               idEvaluationType,
                                                                                               academicYear))]

            i = 0 # contador
            while i <= 10:
                bars.append(GraphBar(score=i, studentCount=await self._getCountStudentsByScoreUsecase(i, codeSubject,
                                                                                                       idEvaluationType,
                                                                                                       academicYear)))
                i += 0.5 # incremento

            return Ok(BarChart(bars=bars,
                               curseStudentCount=courseCount))

        except NoItemsFound as e:
            return NotFound('(GetCountStudentsByScoreController) No students found for grade -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
