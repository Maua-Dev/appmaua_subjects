from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest
from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.main.subjects.module import Modular
from src.main.helpers.status import status as st
from src.adapters.controllers.get_count_students_by_score_controller import GetCountStudentsByScoreController

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

@app.get("/estatistica/{codeSubject}/{idEvaluationType}/{academicYear}")
async def getCountStudentsByScore(codeSubject: str, idEvaluationType: int, academicYear: int, response: Response):
    getCountStudentsByScoreController = Modular.getInject(GetCountStudentsByScoreController)
    req = HttpRequest(query={'codeSubject': codeSubject,
                             'idEvaluationType': idEvaluationType,
                             'academicYear': academicYear})
    result = await getCountStudentsByScoreController(req)
    response.status_code = st.get(result.status_code)
    return result

