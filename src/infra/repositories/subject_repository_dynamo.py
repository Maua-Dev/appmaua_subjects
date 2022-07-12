from typing import List
import os
from boto3 import resource
import boto3
from boto3.dynamodb.conditions import Key

from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.envs import Envs
from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.infra.dtos.subject_dynamo_dto import SubjectDynamoDTO


class SubjectRepositoryDynamo(ISubjectRepository):
    dynamo: DynamoDatasource

    def __init__(self):
        self.dynamo = DynamoDatasource(access_key=Envs.getConfig().access_key,
                                       secret_key=Envs.getConfig().secret_key,
                                       endpoint_url=Envs.getConfig().endpoint_url,
                                       dynamo_table_name=Envs.getConfig().dynamo_table_name,
                                       region=Envs.getConfig().region)

    async def get_all_subjects(self) -> List[Subject]:
        data = await self.dynamo.getAllItems()

        subjects = []
        for item in data:
            dto = SubjectDynamoDTO.fromDynamo(item)
            subjects.append(dto.toEntity())

        return subjects

    async def get_subjects_by_student(self, ra: str) -> List[Subject]:
        keyCondition = Key("studentRA").eq(ra)
        data = await self.dynamo.query(keyConditionExpression=keyCondition, IndexName="studentRA-index")

        subjects = []
        for item in data:
            dto = SubjectDynamoDTO.fromDynamo(item)
            subjects.append(dto.toEntity())

        return subjects

    async def get_subject(self, ra: str, code: str) -> Subject:
        data = await self.dynamo.getItem(key={
            "subjectCode": code,
            "studentRA": ra
        })
        dto = SubjectDynamoDTO.fromDynamo(data["Item"])
        return dto.toEntity()


