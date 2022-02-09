from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_subject_by_professor_id_usecase import GetSubjectByProfessorIdUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class GetSubjectByProfessorIdController:
    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._getSubjectByProfessorIdUsecase = GetSubjectByProfessorIdUsecase(subjectRepository)

    def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['idProfessor'] is None or req.query['idProfessor'] == 0:
                return BadRequest(f"idProfessor is invalid. (idStudent = {req.query['idProfessor']})")

            if type(req.query['idProfessor']) is not int:
                return BadRequest('idProfessor must be int.')

            idProfessor = req.query['idProfessor']

            subjects, count = self._getSubjectByProfessorIdUsecase(idProfessor)

            response = {"subjects": subjects, "count": count}

            return Ok(response)

        except NoItemsFound:
            return NoContent()

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)