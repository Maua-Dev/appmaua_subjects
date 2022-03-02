import pytest
from fastapi.testclient import TestClient
from fastapi import status, FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse

from src.adapters.controllers.get_all_subjects_controller import GetAllSubjectsController
from src.adapters.controllers.get_count_students_by_score_controller import GetCountStudentsByScoreController
from src.adapters.controllers.get_student_subject_scores_controller import GetStudentSubjectScoreController
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.controllers.get_subject_by_code_controller import GetSubjectByCodeController
from src.adapters.controllers.get_subject_by_professor_id_controller import GetSubjectByProfessorIdController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest
from src.envs import EnvEnum, Envs
from src.main.helpers.status import status as st
from src.main.subjects.module import Modular

Envs.appEnv = EnvEnum.MOCK
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


@app.get("/notas/{idStudent}/{codeSubject}/{academicYear}")
async def getCountStudentsByScore(codeSubject: str, idStudent: int, academicYear: int, response: Response):
    getStudentSubjectScoreController = Modular.getInject(GetStudentSubjectScoreController)
    req = HttpRequest(query={'codeSubject': codeSubject,
                             'idStudent': idStudent,
                             'academicYear': academicYear})
    result = await getStudentSubjectScoreController(req)
    response.status_code = st.get(result.status_code)
    return result


client = TestClient(app)


def test_read_scores():
    response = client.get("/notas/1/ecm505/2022")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status_code": 200,
        "body": {
            "name": "Banco de dados",
            "finalScore": 8.9,
            "isPartialScore": False,
            "tests": [
                {
                    "idEvalType": 1,
                    "value": 9.5
                },
                {
                    "idEvalType": 2,
                    "value": 8.5
                }
            ],
            "works": [
                {
                    "idEvalType": 7,
                    "value": 9.5
                },
                {
                    "idEvalType": 8,
                    "value": 7.0
                },
                {
                    "idEvalType": 9,
                    "value": 7.0
                },
                {
                    "idEvalType": 10,
                    "value": 9.0
                }
            ],
            "subs": [
                {
                    "idEvalType": 5,
                    "value": 9.5
                }
            ]
        }
    }


def test_read_bar_chart_data():
    response = client.get("/estatistica/ecm505/1/2022")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status_code": 200,
        "body": {
            "bars": [
                {
                    "score": -2.0,
                    "studentCount": 0
                },
                {
                    "score": -1.0,
                    "studentCount": 0
                },
                {
                    "score": 0.0,
                    "studentCount": 0
                },
                {
                    "score": 0.5,
                    "studentCount": 0
                },
                {
                    "score": 1.0,
                    "studentCount": 0
                },
                {
                    "score": 1.5,
                    "studentCount": 0
                },
                {
                    "score": 2.0,
                    "studentCount": 0
                },
                {
                    "score": 2.5,
                    "studentCount": 0
                },
                {
                    "score": 3.0,
                    "studentCount": 0
                },
                {
                    "score": 3.5,
                    "studentCount": 0
                },
                {
                    "score": 4.0,
                    "studentCount": 0
                },
                {
                    "score": 4.5,
                    "studentCount": 0
                },
                {
                    "score": 5.0,
                    "studentCount": 0
                },
                {
                    "score": 5.5,
                    "studentCount": 0
                },
                {
                    "score": 6.0,
                    "studentCount": 0
                },
                {
                    "score": 6.5,
                    "studentCount": 0
                },
                {
                    "score": 7.0,
                    "studentCount": 0
                },
                {
                    "score": 7.5,
                    "studentCount": 0
                },
                {
                    "score": 8.0,
                    "studentCount": 0
                },
                {
                    "score": 8.5,
                    "studentCount": 0
                },
                {
                    "score": 9.0,
                    "studentCount": 0
                },
                {
                    "score": 9.5,
                    "studentCount": 2
                },
                {
                    "score": 10.0,
                    "studentCount": 0
                }
            ]
        }
    }


def test_read_all_subjects():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status_code": 200,
        "body": [
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
        ]
    }


def test_read_student_subjects():
    response = client.get("/student/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status_code": 200,
        "body": [
            {
                "codeSubject": "ECM501",
                "name": "Ciencia de dados"
            },
            {
                "codeSubject": "ECM502",
                "name": "Devops"
            }
        ]
    }


def test_read_subject_by_code():
    response = client.get("/subject/ecm505")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "status_code": 200,
        "body": {
            "codeSubject": "ECM505",
            "name": "Banco de dados"
        }
    }


def test_read_subject_by_professor_id():
    response = client.get("/professor/1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        'body': [{
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
        'status_code': 200
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
