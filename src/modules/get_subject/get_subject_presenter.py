import asyncio

from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.modules.get_subject.get_subject_usecase import GetSubjectUsecase

repo = SubjectRepositoryDynamo()

usecase = GetSubjectUsecase(repo)


print(asyncio.run(usecase("17.00163-3", "ECM502")))