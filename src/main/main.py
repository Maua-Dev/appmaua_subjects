from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adapters.errors.http_exception import HttpException
from src.adapters.helpers.http_models import HttpRequest

from src.adapters.viewmodels.average_subjects_viewmodel import AverageSubjectsViewModel

from src.main.helpers.status import status
from src.main.subjects.module import Modular


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

@app.get("/Subjects/{idStudent}",response_model=AverageSubjectsViewModel)
def getStudentSubjectsById(idStudent: int, response: Response):
    query = {
        'idStudent': idStudent
    }
    getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)    
    result = getStudentSubjectsController(req=HttpRequest(query=query))    
    response.status_code = status.get(result.status_code)    
    return result.body