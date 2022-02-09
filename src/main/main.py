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
from src.main.helpers.status import status

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
def getAllSubjects(response: Response):
    getAllSubjectsController = Modular.getInject(GetAllSubjectsController)
    req = HttpRequest(query=None)
    result = getAllSubjectsController(req)
    response.status_code = status.get(result.status_code)
    return result.body


@app.get("/student/{idStudent}")
def getStudentSubjects(idStudent: int, response: Response):
    getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)
    req = HttpRequest(query={'idStudent': idStudent})
    result = getStudentSubjectsController(req)
    response.status_code = status.get(result.status_code)
    return result.body


@app.get("/subject/{codeSubject}")
def getSubjectByCode(codeSubject: str, response: Response):
    getSubjectByCodeController = Modular.getInject(GetSubjectByCodeController)
    req = HttpRequest(query={'codeSubject': codeSubject})
    result = getSubjectByCodeController(req)
    response.status_code = status.get(result.status_code)
    return result.body


@app.get("/professor/{idProfessor}")
def getSubjectByProfessorId(idProfessor: int, response: Response):
    getSubjectByProfessorIdController = Modular.getInject(GetSubjectByProfessorIdController)
    req = HttpRequest(query={'idProfessor': idProfessor})
    result = getSubjectByProfessorIdController(req)
    response.status_code = status.get(result.status_code)
    return result.body
