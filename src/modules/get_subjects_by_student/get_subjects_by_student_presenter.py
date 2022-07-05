from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_subjects_by_student.get_subjects_by_student_controller import GetSubjectsByStudentController
from src.modules.get_subjects_by_student.get_subjects_by_student_usecase import GetSubjectsByStudentUsecase


async def lambda_handler(event, context):
    repo = SubjectRepositoryDynamo()
    #repo = SubjectRepositoryMock()
    usecase = GetSubjectsByStudentUsecase(repo)
    controller = GetSubjectsByStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()


