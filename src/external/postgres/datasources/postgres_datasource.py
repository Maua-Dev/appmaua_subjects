from typing import List

from sqlalchemy.future import select
from src.external.postgres.db_config_async import AsyncDBConnectionHandler
from src.infra.datasources.datasource_interface import IDataSource
from src.infra.dtos.Subject import *
from src.infra.dtos.Subject.course_dto import CourseDTO
from src.infra.dtos.Subject.student_course_dto import StudentCourseDTO


class PostgresDataSource(IDataSource):

    async def getSubjectsByStudent(self, idStudent: int) -> List[SubjectDTO]:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                        join(SubjectDTO.students).
                        where(StudentSubjectDTO.idStudent == idStudent)
                )

                return query.scalars().all()
            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getSubjectsByCode(self, codeSubject: str) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                        where(SubjectDTO.codeSubject == codeSubject)
                )
                return query.scalars().first()
            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getSubjectStudents(self, codeSubject: str) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                        where(SubjectDTO.codeSubject == codeSubject)
                )

                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
        pass

    async def getAllSubjects(self) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO)
                )

                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
        pass

    async def getSubjectByProfessorId(self, idProfessor: int) -> SubjectDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(SubjectDTO).
                        join(SubjectDTO.professors).
                        where(ProfessorSubjectDTO.idProfessor == idProfessor)
                )

                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getCountStudentsByScore(self, gradeValue: float, codeSubject: str, idEvaluationType: int,
                                      academicYear: int, courseId: int, courseYear: int) -> StudentScoresDTO:

        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(StudentScoresDTO).
                    join(StudentCourseDTO, StudentCourseDTO.idStudent == StudentScoresDTO.idStudent).
                        where(StudentScoresDTO.codeSubject == codeSubject,
                              StudentScoresDTO.idEvaluationType == idEvaluationType,
                              StudentScoresDTO.academicYear == academicYear,
                              StudentScoresDTO.value == gradeValue,
                              StudentCourseDTO.idCourse == courseId,
                              StudentCourseDTO.courseYear == courseYear)
                )

                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getSubjectScoreByEvalType(self, codeSubject: str, idStudent: int, academicYear: int,
                                        idEvaluationType: int) -> StudentScoresDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(StudentScoresDTO).
                        where(StudentScoresDTO.codeSubject == codeSubject,
                              StudentScoresDTO.idEvaluationType == idEvaluationType,
                              StudentScoresDTO.academicYear == academicYear,
                              StudentScoresDTO.idStudent == idStudent)
                )

                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getEvalQuantityByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalDataDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(EvalDataDTO).
                        where(EvalDataDTO.codeSubject == codeSubject,
                              EvalDataDTO.academicYear == academicYear,
                              EvalDataDTO.idEvaluationType == idEvaluationType)
                )

                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getEvalWeightByType(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalWeightDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(EvalWeightDTO).
                        where(EvalWeightDTO.codeSubject == codeSubject,
                              EvalWeightDTO.academicYear == academicYear,
                              EvalWeightDTO.idEvaluationType == idEvaluationType)
                )

                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getWichScoreToReplace(self, codeSubject: str, academicYear: int, idEvaluationType: int) -> EvalWeightDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(EvalWeightDTO).
                        where(EvalWeightDTO.codeSubject == codeSubject,
                              EvalWeightDTO.academicYear == academicYear,
                              EvalWeightDTO.idEvaluationType == idEvaluationType)
                )

                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getCountStudentsByCourse(self, idCourse: int, courseYear: int, academicYear: int) -> StudentCourseDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(StudentCourseDTO).
                        where(StudentCourseDTO.idCourse == idCourse,
                              StudentCourseDTO.courseYear == courseYear,
                              StudentCourseDTO.academicYear == academicYear)
                )
                return query.scalars().all()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getStudentCourseId(self, idStudent: int, academicYear: int) -> StudentCourseDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(StudentCourseDTO).
                        where(StudentCourseDTO.idStudent == idStudent,
                              StudentCourseDTO.academicYear == academicYear)
                )
                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getStudentCourseYear(self, idStudent: int, academicYear: int) -> StudentCourseDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(StudentCourseDTO).
                        where(StudentCourseDTO.idStudent == idStudent,
                              StudentCourseDTO.academicYear == academicYear)
                )
                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')

    async def getCourseName(self, idCourse: int) -> CourseDTO:
        async with AsyncDBConnectionHandler().session() as s:
            try:
                query = await s.execute(
                    select(CourseDTO).
                        where(CourseDTO.id == idCourse)
                )
                return query.scalars().first()

            except Exception as e:
                raise Exception(f'DataSource Error. {str(e)}')
