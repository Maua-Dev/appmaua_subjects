from typing import List
import os
from boto3 import resource
import boto3

from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.external.dynamo.datasources.dynamo_datasource import DynamoDatasource
from src.infra.dtos.subject_dynamo_dto import SubjectDynamoDTO


class SubjectRepositoryDynamo(ISubjectRepository):
    dynamo: DynamoDatasource

    def __init__(self):
        self.dynamo = DynamoDatasource(access_key=None, secret_key=None, endpoint_url=None, dynamo_table_name="IaCStack-MauAppSubjectsDB1BBD4F9F-QNRBDUJG0XGQ") #TODO COLOCAR NO .ENV PELO AMOR DE DEUS


    async def get_all_subjects(self) -> List[Subject]:
        data = await self.dynamo.getAllItems()

        subjects = []
        for item in data:
            dto = SubjectDynamoDTO.fromDynamo(item)
            subjects.append(dto.toEntity())

        return subjects

    async def get_subjects_by_student(self, ra: str) -> List[Subject]:
        pass

    async def get_subject(self, ra: str, code: str) -> Subject:
        pass


