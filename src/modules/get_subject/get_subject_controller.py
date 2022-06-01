from src.modules.get_subject.get_subject_usecase import GetSubjectUsecase
from src.modules.get_subject.get_subject_viewmodel import GetSubjectViewmodel
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.errors.domain_errors import NoItemsFound




class GetSubjectController:
    def __init__(self, usecase:GetSubjectUsecase):
        self.getSubjectUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            subject = await self.getSubjectUsecase(ra=request.query_params["ra"],
                                                   code=request.query_params["code"])
            viewModel = GetSubjectViewmodel(subject)
            return OK(viewModel.to_dict())

        except NoItemsFound as err:
            return HttpResponse(
                status_code=404,
                body=err.message
            )