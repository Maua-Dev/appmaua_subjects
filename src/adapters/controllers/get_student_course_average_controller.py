from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.repositories.subject_repository_interface import ISubjectRepository


from src.adapters.helpers.http_models import *

class GetStudentCourseAverageController:
    def __init__(self) -> None:
        pass

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        pass