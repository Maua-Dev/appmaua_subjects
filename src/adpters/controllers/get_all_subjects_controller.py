from src.adpters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.adpters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok


class GetStudentSubjectsController:
    def __init__(self, getAllSubjectsUsecase: GetAllSubjectsUsecase) -> None:
        self._getAllSubjectsUsecase = getAllSubjectsUsecase

    def __call__(self, req: HttpRequest) -> HttpResponse:

        if type(req.query) is not None:
            return BadRequest('No parameters allowed.')

        try:
            subjects = self._getAllSubjectsUsecase()
            response = {"subjects": subjects}
            return Ok(response)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)