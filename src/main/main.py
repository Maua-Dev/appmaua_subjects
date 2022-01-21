from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from src.adpters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adpters.helpers.http_models import HttpRequest

from src.adpters.viewmodels.average_subjects_viewmodel import AverageSubjectsViewModel

from src.main.helpers.status import status
from src.main.subjects.module import Modular

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/Subjects/{idStudent}",response_model=AverageSubjectsViewModel)
def getStudentSubjectsById(idStudent: int, response: Response):
    query = {
        'idStudent': idStudent
    }
    getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)    
    response = getStudentSubjectsController(req=HttpRequest(query=query))
    response.status_code = status.get(response.status_code)
    return response.body