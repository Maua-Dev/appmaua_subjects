
import asyncio

from src.helpers.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.modules.get_all_subjects.get_all_subjects_controller import GetAllSubjectsController
from src.modules.get_all_subjects.get_all_subjects_usecase import GetAllSubjectsUsecase
from src.envs import Envs

async def lambda_handler(event, context):
    repo = SubjectRepositoryMock() if Envs.IsMock() else SubjectRepositoryDynamo()
    usecase = GetAllSubjectsUsecase(repo)
    controller = GetAllSubjectsController(usecase)

    httpRequest = LambdaHttpRequest(data=event)
    response = await controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
