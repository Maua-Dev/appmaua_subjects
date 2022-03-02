from src.adapters.errors.http_exception import HttpException
from src.domain.errors.errors import UnexpectedError, NoItemsFound
from src.domain.usecases.get_final_score_usecase import GetFinalScoreUsecase
from src.domain.usecases.get_student_subject_score_usecase import GetStudentSubjectScoreUsecase
from src.domain.usecases.get_subject_evaluation_quantity_usecase import GetSubjectEvaluationQuantityUsecase
from src.adapters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok, NoContent
from src.adapters.viewmodels.subject_scores import *
from src.domain.usecases.get_subject_by_code_usecase import GetSubjectByCodeUsecase
from src.domain.entities.subject import Subject


class GetStudentSubjectScoreController:
    def __init__(self,
                 getStudentSubjectScoreUsecase: GetStudentSubjectScoreUsecase,
                 getSubjectByCodeUsecase: GetSubjectByCodeUsecase,
                 getFinalScoreUsecase: GetFinalScoreUsecase,
                 getSubjectEvaluationQuantityUsecase: GetSubjectEvaluationQuantityUsecase) -> None:

        self._getStudentSubjectScoreUsecase = getStudentSubjectScoreUsecase
        self._getSubjectByCodeUsecase = getSubjectByCodeUsecase
        self._getFinalScoreUsecase = getFinalScoreUsecase
        self._getSubjectEvaluationQuantityUsecase = getSubjectEvaluationQuantityUsecase

    async def __call__(self, req: HttpRequest) -> HttpResponse:
        try:
            if req.query['codeSubject'] is None :
                return BadRequest(f"codeSubject is invalid. (codeSubject = None)")

            if req.query['academicYear'] is None:
                return BadRequest(f"academicYear is invalid. (academicYear = None)")

            if req.query['idStudent'] is None:
                return BadRequest(f"idStudent is invalid. (academicYear = None)")

            codeSubject = req.query['codeSubject'].upper()
            academicYear = req.query['academicYear']
            idStudent = req.query['idStudent']

            subject: Subject = await self._getSubjectByCodeUsecase(codeSubject)
            name = subject.name

            finalScore, isPartialScore = await self._getFinalScoreUsecase(codeSubject, academicYear, idStudent)

            workQnt = await self._getSubjectEvaluationQuantityUsecase(codeSubject, academicYear, 19)
            testQnt = await self._getSubjectEvaluationQuantityUsecase(codeSubject, academicYear, 20)
            subQnt = await self._getSubjectEvaluationQuantityUsecase(codeSubject, academicYear, 21)

            tests = []
            works = []
            subs = []

            for i in range(1, testQnt + 1):
                tests.append(ScoreModel(idEvalType=i,
                                        value=await self._getStudentSubjectScoreUsecase(codeSubject.upper(),
                                                                                        idStudent,
                                                                                        academicYear,
                                                                                        i)))
                # index da lista define a prova
                # tests[n] = P(n+1)

            for j in range(7, workQnt + 7):
                works.append(ScoreModel(idEvalType=j,
                                        value=await self._getStudentSubjectScoreUsecase(codeSubject.upper(),
                                                                                        idStudent,
                                                                                        academicYear,
                                                                                        j)))
                # index da lista define o trabalho
                # works[n] = T(n+1)

            for k in range(5, subQnt + 5):
                subs.append(ScoreModel(idEvalType=k,
                                        value=await self._getStudentSubjectScoreUsecase(codeSubject.upper(),
                                                                                        idStudent,
                                                                                        academicYear,
                                                                                        k)))
                # index da lista define a sub
                # subScores[n] = PS(n+1)

            return Ok(SubjectScores(name=name,
                                    finalScore=finalScore,
                                    isPartialScore=isPartialScore,
                                    tests=tests,
                                    works=works,
                                    subs=subs))

        except NoItemsFound:
            return NoContent()

        except UnexpectedError as e:
            err = InternalServerError(e.message)
            return HttpException(message=err.body, status_code=err.status_code)
