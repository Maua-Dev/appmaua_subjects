from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.usecases.get_count_students_by_score_usecase import GetCountStudentsByScoreUsecase
from src.adapters.helpers.http_models import *
from src.adapters.viewmodels.bar_chart import *


class GetCountStudentsByScoreController:
    def __init__(self, getCountStudentsByScoreUsecase: GetCountStudentsByScoreUsecase) -> None:
        self._getCountStudentsByScoreUsecase = getCountStudentsByScoreUsecase
    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['codeSubject'] is None :
                return BadRequest(f"codeSubject is invalid. (codeSubject = None)")

            if req.query['idEvaluationType'] is None:
                return BadRequest(f"idEvaluationType is invalid. (idEvaluationType = None)")

            if req.query['academicYear'] is None:
                return BadRequest(f"academicYear is invalid. (academicYear = None)")

            codeSubject = req.query['codeSubject']
            idEvaluationType = req.query['idEvaluationType']
            academicYear = req.query['academicYear']

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

            return Ok(BarChart(bars=bars))

        except NoItemsFound as e:
            return NotFound('(GetCountStudentsByScoreController) No students found for grade -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
