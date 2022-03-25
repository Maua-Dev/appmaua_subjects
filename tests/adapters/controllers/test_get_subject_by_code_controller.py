import pytest
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.infra.repositories.subject_repository_mock import SubjectRepositoryMock
from src.adapters.helpers.http_models import *
from src.domain.entities.subject import Subject

class Test_GetSubjectByCodeController:

    @pytest.mark.asyncio
    async def test_get_subject_by_code_controller(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 'ecm505'})
        answer = await getSubjectByCodeController(req)
        
        assert type(answer.body) is Subject        
        assert answer.status_code == 200

    @pytest.mark.asyncio
    async def test_get_subject_by_code_controller_no_item_found(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 'esm505'})
        answer = await getSubjectByCodeController(req)

        assert type(answer) is NotFound
        assert answer.status_code == 404

    @pytest.mark.asyncio
    async def test_get_subject_by_code_controller_error(self):
        getSubjectByCodeController = GetSubjectByCodeController(getSubjectByCodeUsecase=GetSubjectByCodeUsecase(subjectRepository=SubjectRepositoryMock()))
        req = HttpRequest(query={'codeSubject': 2})
        answer = await getSubjectByCodeController(req)

        assert type(answer) is BadRequest
        assert answer.status_code == 400
