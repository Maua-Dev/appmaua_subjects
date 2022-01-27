from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from src.adpters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.adpters.errors.http_exception import HttpException
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



@app.exception_handler(HttpException)
async def internal_exception_handler(request: Request, exc: HttpException):
    return PlainTextResponse(exc.body, status_code=exc.status_code)

@app.get("/Subjects/{idStudent}",response_model=AverageSubjectsViewModel)
async def getStudentSubjectsById(idStudent: int, response: Response):
    query = {
        'idStudent': idStudent
    }
    getStudentSubjectsController = Modular.getInject(GetStudentSubjectsController)    
    result = await getStudentSubjectsController(req=HttpRequest(query=query))    
    response.status_code = status.get(result.status_code)    
    return result.body