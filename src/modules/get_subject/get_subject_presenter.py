import asyncio

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_subject.get_subject_controller import GetSubjectController
from src.modules.get_subject.get_subject_usecase import GetSubjectUsecase



async def lambda_handler(event, context):
    #repo = SubjectRepositoryDynamo()
    repo = SubjectRepositoryMock()
    usecase = GetSubjectUsecase(repo)
    controller = GetSubjectController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()