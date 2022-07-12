from src.envs import Envs
from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from get_subjects_by_student_controller import GetSubjectsByStudentController
from get_subjects_by_student_usecase import GetSubjectsByStudentUsecase
import asyncio


def lambda_handler(event, context):
    repo = SubjectRepositoryMock() if Envs.IsMock() else SubjectRepositoryDynamo()
    usecase = GetSubjectsByStudentUsecase(repo)
    controller = GetSubjectsByStudentController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = asyncio.run(controller(httpRequest))
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()


