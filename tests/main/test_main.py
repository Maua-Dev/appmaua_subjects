from fastapi.testclient import TestClient
from fastapi import status, FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest
from src.envs import EnvEnum, Envs
from src.main.helpers.status import status as st
from src.main.subjects.module import Modular
from src.main.main import app
Envs.appEnv = EnvEnum.MOCK
# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_methods=["*"],
#     allow_headers=["*"],
# )


# @app.exception_handler(HttpException)
# async def internal_exception_handler(request: Request, exc: HttpException):
#     return PlainTextResponse(exc.body, status_code=exc.status_code)


# @app.get("/")
# def getAllSubjects(response: Response):    
#     getAllSubjectsController = Modular.getInject(GetAllSubjectsController)
#     req = HttpRequest(query=None)
#     result = getAllSubjectsController(req)
#     response.status_code = st.get(result.status_code)
#     return result


# @app.get("/student/{idStudent}")
# def getStudentSubjects(idStudent: int, response: Response):
#     getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)
#     req = HttpRequest(query={'idStudent': idStudent})
#     result = getStudentSubjectsController(req)
#     response.status_code = st.get(result.status_code)
#     return result


# @app.get("/subject/{codeSubject}")
# def getSubjectByCode(codeSubject: str, response: Response):
#     Envs.appEnv = EnvEnum.MOCK
#     getSubjectByCodeController = Modular.getInject(GetSubjectByCodeController)
#     req = HttpRequest(query={'codeSubject': codeSubject})
#     result = getSubjectByCodeController(req)
#     response.status_code = st.get(result.status_code)
#     return result


# @app.get("/professor/{idProfessor}")
# def getSubjectByProfessorId(idProfessor: int, response: Response):
#     getSubjectByProfessorIdController = Modular.getInject(GetSubjectByProfessorIdController)
#     req = HttpRequest(query={'idProfessor': idProfessor})
#     result = getSubjectByProfessorIdController(req)
#     response.status_code = st.get(result.status_code)
#     return result

client = TestClient(app)


def test_read_all_subjects():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
                                  "status_code": 200,
                                  "body": {
                                    "subjects": [
                                      {
                                        "codeSubject": "ECM501",
                                        "name": "Ciencia de dados"
                                      },
                                      {
                                        "codeSubject": "ECM502",
                                        "name": "Devops"
                                      },
                                      {
                                        "codeSubject": "ECM504",
                                        "name": "IA"
                                      },
                                      {
                                        "codeSubject": "ECM505",
                                        "name": "Banco de dados"
                                      },
                                      {
                                        "codeSubject": "ECM503",
                                        "name": "Controladores"
                                      }
                                    ],
                                    "count": 5
                                  }
                                }


def test_read_student_subjects():
    response = client.get("/student/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [
                                {
                                  "codeSubject": "ECM501",
                                  "name": "Ciencia de dados"
                                },
                                {
                                  "codeSubject": "ECM502",
                                  "name": "Devops"
                                }
                              ]


def test_read_subject_by_code():
    response = client.get("/subject/ecm505")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
                                "codeSubject": "ECM505",
                                "name": "Banco de dados"
                              }


def test_read_subject_by_professor_id():
    response = client.get("/professor/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
                                  "status_code": 200,
                                  "body": {
                                    "subjects": [
                                      {
                                        "codeSubject": "ECM501",
                                        "name": "Ciencia de dados"
                                      },
                                      {
                                        "codeSubject": "ECM502",
                                        "name": "Devops"
                                      },
                                      {
                                        "codeSubject": "ECM504",
                                        "name": "IA"
                                      }
                                    ],
                                    "count": 3
                                  }
                                }


def test_read_student_subjects_no_content():
    response = client.get("/student/10")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_read_subject_by_code_no_content():
    response = client.get("/subject/ecm5050")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_read_subject_by_professor_id_no_content():
    response = client.get("/professor/10")
    assert response.status_code == status.HTTP_204_NO_CONTENT


def test_read_student_subjects_bad_request():
    response = client.get("/student/0")
    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_read_subject_by_professor_id_bad_request():
    response = client.get("/professor/0")
    assert response.status_code == status.HTTP_400_BAD_REQUEST