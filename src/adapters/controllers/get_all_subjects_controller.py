from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class GetStudentSubjectsController:
    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._getAllSubjectsUsecase = GetAllSubjectsUsecase(subjectRepository)

    def __call__(self, req: HttpRequest) -> HttpResponse:

        if req.query is not None:
            return BadRequest('No parameters allowed.')

        try:
            subjects = self._getAllSubjectsUsecase()
            response = {"subjects": subjects, "count": len(subjects)}
            return Ok(response)

        except NoItemsFound:
            return NoContent()

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)