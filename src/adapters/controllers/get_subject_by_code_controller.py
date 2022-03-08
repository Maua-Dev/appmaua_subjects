from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class GetSubjectByCodeController:
    def __init__(self, getSubjectByCodeUsecase: GetSubjectByCodeUsecase) -> None:
        self._getSubjectByCodeUsecase = getSubjectByCodeUsecase

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['codeSubject'] is None:
                return BadRequest('codeSubject is null.')

            if type(req.query['codeSubject']) is not str:
                return BadRequest('codeSubject must be str.')

            codeSubject = req.query['codeSubject']

            subject = await self._getSubjectByCodeUsecase(codeSubject)            

            return Ok(subject)

        except NoItemsFound:
            return NoContent()

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
