from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.adapters.controllers.get_student_subject_scores_controller import GetStudentSubjectScoreController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest
from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.main.subjects.module import Modular
from src.main.helpers.status import status as st
from src.adapters.controllers.get_score_statistics_controller import GetScoreStatisticsController
from src.adapters.controllers.get_student_course_average_controller import GetStudentCourseAverageController


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HttpException)
async def internal_exception_handler(request: Request, exc: HttpException):

    return PlainTextResponse(exc.body, status_code=exc.status_code)

@app.get("/")
async def getAllSubjects(response: Response):

    getAllSubjectsController = Modular.getInject(GetAllSubjectsController)
    req = HttpRequest(query=None)
    result = await getAllSubjectsController(req)
    response.status_code = st.get(result.status_code)
    return result


@app.get("/student/{idStudent}")
async def getStudentSubjects(idStudent: int, response: Response):

    getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)
    req = HttpRequest(query={'idStudent': idStudent})
    result = await getStudentSubjectsController(req)
    response.status_code = st.get(result.status_code)
    return result


@app.get("/subject/{codeSubject}")
async def getSubjectByCode(codeSubject: str, response: Response):

    getSubjectByCodeController = Modular.getInject(GetSubjectByCodeController)
    req = HttpRequest(query={'codeSubject': codeSubject})
    result = await getSubjectByCodeController(req)
    response.status_code = st.get(result.status_code)
    return result

@app.get("/professor/{idProfessor}")
async def getSubjectByProfessorId(idProfessor: int, response: Response):

    getSubjectByProfessorIdController = Modular.getInject(GetSubjectByProfessorIdController)
    req = HttpRequest(query={'idProfessor': idProfessor})
    result = await getSubjectByProfessorIdController(req)
    response.status_code = st.get(result.status_code)
    return result

@app.get("/estatistica/{codeSubject}/{idEvaluationType}/{academicYear}/{idStudent}")
async def getCountStudentsByScore(codeSubject: str, idEvaluationType: int, academicYear: int, idStudent: int,
                                  response: Response):

    getCountStudentsByScoreController = Modular.getInject(GetScoreStatisticsController)
    req = HttpRequest(query={'codeSubject': codeSubject,
                             'idEvaluationType': idEvaluationType,
                             'academicYear': academicYear,
                             'idStudent': idStudent})
    result = await getCountStudentsByScoreController(req)
    response.status_code = st.get(result.status_code)
    return result

@app.get("/notas/{idStudent}/{codeSubject}/{academicYear}")
async def getCountStudentsByScore(codeSubject: str, idStudent: int, academicYear: int, response: Response):

    getStudentSubjectScoreController = Modular.getInject(GetStudentSubjectScoreController)
    req = HttpRequest(query={'codeSubject': codeSubject,
                             'idStudent': idStudent,
                             'academicYear': academicYear})
    result = await getStudentSubjectScoreController(req)
    response.status_code = st.get(result.status_code)
    return result

@app.get("/notas-gerais/{idStudent}/{academicYear}")
async def GetStudentCourseAverage(idStudent: int, academicYear: int, response: Response):

    getStudentCourseAverageController = Modular.getInject(GetStudentCourseAverageController)
    req = HttpRequest(query={'idStudent': idStudent,
                             'academicYear': academicYear})
    result = await getStudentCourseAverageController(req)
    response.status_code = st.get(result.status_code)
    return result