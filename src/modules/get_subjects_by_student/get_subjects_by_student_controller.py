from src.helpers.errors.domain_errors import NoItemsFound
from src.helpers.http_models import HttpRequest, HttpResponse, OK
from src.modules.get_subjects_by_student.get_subjects_by_student_usecase import GetSubjectsByStudentUsecase
from src.modules.get_subjects_by_student.get_subjects_by_student_viewmodel import GetSubjectsByStudentViewmodel


class GetSubjectsByStudentController:

    def __init__(self, usecase:GetSubjectsByStudentUsecase):
        self.getSubjectsByStudentUsecase = usecase

    async def __call__(self, request: HttpRequest) -> HttpResponse:
        try:

            subjects = await self.getSubjectsByStudentUsecase(ra=request.query_params["ra"])
            viewModel = GetSubjectsByStudentViewmodel(subjects)
            return OK(viewModel.to_dict())

        except NoItemsFound as err:
            return HttpResponse(
                status_code=404,
                body=err.message
            )