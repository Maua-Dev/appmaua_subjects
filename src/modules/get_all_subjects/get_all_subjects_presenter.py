import pprint
import asyncio

from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.modules.get_all_subjects.get_all_subjects_usecase import GetAllSubjectsUsecase

repo = SubjectRepositoryDynamo()

usecase = GetAllSubjectsUsecase(repo)


a = asyncio.run(usecase())

print(a)
