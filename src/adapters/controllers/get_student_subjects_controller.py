from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class GetStudentSubjectsController:
    def __init__(self, getStudentSubjectsUsecase: GetStudentSubjectsUsecase) -> None:
        self._getStudentSubjectsUsecase = getStudentSubjectsUsecase

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['idStudent'] is None or req.query['idStudent'] == 0:
                return BadRequest(f"idStudent is invalid. (idStudent = {req.query['idStudent']})")

            if type(req.query['idStudent']) is not int:
                return BadRequest('idStudent must be int.')

            idStudent = req.query['idStudent']

            subjects = await self._getStudentSubjectsUsecase(idStudent)

            return Ok(subjects)

        except NoItemsFound:
            return NoContent()

        except UnexpectedError as e:  
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
