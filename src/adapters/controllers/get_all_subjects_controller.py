from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.adapters.helpers.http_models import *


class GetAllSubjectsController:
    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._getAllSubjectsUsecase = GetAllSubjectsUsecase(subjectRepository)

    async def __call__(self, req: HttpRequest) -> HttpResponse:

        if req.query is not None:
            return BadRequest('No parameters allowed.')

        try:
            subjects = await self._getAllSubjectsUsecase()

            return Ok(subjects)

        except NoItemsFound as e:
            return NotFound('(GetAllSubjectsController) No subjects found -> ' + e.message)

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)