from src.helpers.errors.domain_errors import NoItemsFound
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.helpers.http_status_code import HttpStatusCode
from src.modules.get_all_subjects.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.modules.get_all_subjects.get_all_subjects_viewmodel import GetAllSubjectsViewmodel


class GetAllSubjectsController:

    def __init__(self, usecase: GetAllSubjectsUsecase):
        self.getAllSubjectsUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            subjects = await self.getAllSubjectsUsecase()
            viewModel = GetAllSubjectsViewmodel(subjects)

            return OK(viewModel.to_dict())


        except NoItemsFound as e:
            return HttpResponse(
                status_code=404,
                body=e.message
            )

        except Exception as err:
            return HttpResponse(
                status_code=HttpStatusCode.INTERNAL_SERVER_ERROR.value,
                body=err.message
            )

