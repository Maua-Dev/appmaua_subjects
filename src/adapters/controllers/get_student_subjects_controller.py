from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent


class GetStudentSubjectsController:
    def __init__(self, subjectRepository: ISubjectRepository) -> None:
        self._getStudentSubjectsUsecase = GetStudentSubjectsUsecase(subjectRepository)

    def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['idStudent'] is None:
                return BadRequest('idStudent is null.')

            idStudent = req.query['idStudent']

            subjects = self._getStudentSubjectsUsecase(idStudent)

            response = {"subjects": subjects, "count": len(subjects)}

            return Ok(response)

        except NoItemsFound as e:
            err = NoContent(e.message)
            return HttpException(message=err.body, status_code=err.status_code)

        except UnexpectedError as e:  
            err = InternalServerError(e.message)
            return HttpException(message=err.body,status_code=err.status_code)
