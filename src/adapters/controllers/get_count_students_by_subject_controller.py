from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.usecases.get_count_students_by_subject_usecase import GetCountStudentsBySubjectUsecase
from src.adapters.helpers.http_models import *
from src.adapters.viewmodels.bar_chart import *


class GetCountStudentsBySubjectController:
    def __init__(self, getCountStudentsBySubjectUsecase: GetCountStudentsBySubjectUsecase) -> None:
        self.getCountStudentsBySubjectUsecase = getCountStudentsBySubjectUsecase
    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:

            if req.query['idSubject'] is None:
                return BadRequest("idSubject is invalid. (idSubject = None)")


            idSubject = req.query['idSubject']

            count = await self.getCountStudentsBySubjectUsecase(idSubject)

            return Ok(count)

        except NoItemsFound as e:
            return NotFound('(GetCountStudentsBySubjectController) No students found for grade -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
