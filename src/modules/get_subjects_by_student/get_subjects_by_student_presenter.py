from src.infra.repositories.subject_repository_dynamo import SubjectRepositoryDynamo
from src.modules.get_subjects_by_student.get_subjects_by_student_usecase import GetSubjectsByStudentUsecase
import asyncio

repo = SubjectRepositoryDynamo()

usecase = GetSubjectsByStudentUsecase(repo)

print(asyncio.run(usecase("17.00163-3"))[1])