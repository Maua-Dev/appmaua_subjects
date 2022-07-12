from src.helpers.errors.controller_erros import MissingParameters
from src.helpers.errors.domain_errors import NoItemsFound
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.http_status_code import HttpStatusCode
from .get_subjects_by_student_usecase import GetSubjectsByStudentUsecase
from .get_subjects_by_student_viewmodel import GetSubjectsByStudentViewmodel


class GetSubjectsByStudentController:

    def __init__(self, usecase:GetSubjectsByStudentUsecase):
        self.getSubjectsByStudentUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            subjects = await self.getSubjectsByStudentUsecase(ra=request.query_params["ra"])
            viewModel = GetSubjectsByStudentViewmodel(subjects)
            return OK(viewModel.to_dict())

        except NoItemsFound as err:
            return HttpResponse(
                status_code=404,
                body=err.message
            )

        except MissingParameters as err:
            return HttpResponse(
                status_code=HttpStatusCode.BAD_REQUEST.value,
                body=err.message
            )

        except Exception as err:
            return HttpResponse(
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
                body=err.args[0]
            )