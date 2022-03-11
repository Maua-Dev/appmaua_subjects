from src.domain.entities.subject import Subject
from src.domain.repositories.subject_repository_interface import ISubjectRepository
from src.infra.datasources.datasource_interface import IDataSource
from typing import List


class SubjectRepositoryImp(ISubjectRepository):
    def __init__(self,datasource: IDataSource) -> None:
        super().__init__()
        self._datasource = datasource
    
    async def getStudentSubjects(self, idStudent: int) -> List[Subject]:
        try:
            response = await self._datasource.getSubjectsByStudent(idStudent=idStudent)
            return list(map(lambda x: x.toEntity(), response))
        except Exception as error:
            raise error

    async def getSubjectStudents(self, codeSubject: str) -> List[int]:
        try:
            response = await self._datasource.getSubjectStudents(codeSubject=codeSubject)
            return list(map(lambda x: x.students, response))
        except Exception as error:
            raise error

    async def getAllSubjects(self) -> List[Subject]:
        try:
            response = await self._datasource.getAllSubjects()
            return list(map(lambda x: x.toEntity(), response))
        except Exception as error:
            raise error

    async def getSubjectByCode(self, codeSubject: str) -> Subject:
        try:
            response = await self._datasource.getSubjectsByCode(codeSubject=codeSubject)
            return response
        except Exception as error:
            raise error

    async def getSubjectByProfessorId(self, idProfessor: int) -> List[Subject]:
        try:
            response = await self._datasource.getSubjectByProfessorId(idProfessor=idProfessor)
            return list(map(lambda x: x.toEntity(), response))
        except Exception as error:
            raise error

    async def getCountStudentsByScore(self, gradeValue:float, codeSubject: str, idEvaluationType: int,
                                     academicYear: int) -> int:
        try:
            response = await self._datasource.getCountStudentsByScore(gradeValue=gradeValue, codeSubject=codeSubject,
                                                                      idEvaluationType=idEvaluationType, academicYear= academicYear)
            return len(list(map(lambda x: x, response)))
        except Exception as error:
            raise error

    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> float:

        return None

    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:

        return None

    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> int:

        return None

    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> List[int]:

        return None