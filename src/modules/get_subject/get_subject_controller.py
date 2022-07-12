from src.helpers.errors.controller_erros import MissingParameters
from src.helpers.http_status_code import HttpStatusCode
from get_subject_usecase import GetSubjectUsecase
from get_subject_viewmodel import GetSubjectViewmodel
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.errors.domain_errors import NoItemsFound




class GetSubjectController:
    def __init__(self, usecase:GetSubjectUsecase):
        self.getSubjectUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            if request.query_params.get('ra') is None:
                raise MissingParameters('ra')

            if request.query_params.get('code') is None:
                raise MissingParameters('code')

            subject = await self.getSubjectUsecase(ra=request.query_params["ra"],
                                                   code=request.query_params["code"])
            viewModel = GetSubjectViewmodel(subject)
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