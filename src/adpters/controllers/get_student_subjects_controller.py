from src.adpters.viewmodels.average_subjects_viewmodel import AverageSubjectsViewModel, AverageViewModel
from src.domain.errors.errors import UnexpectedError
from src.domain.usecases.get_student_subjects_score_usecase import GetStudentSubjectsScoreUsecase
from src.domain.usecases.get_student_subjects_usecase import GetStudentSubjectsUsecase
from src.adpters.helpers.http_models import BadRequest, HttpRequest, HttpResponse, InternalServerError, Ok
from random import randrange
class GetStudentSubjectsController:
    def __init__(self, getStudentSubjects: GetStudentSubjectsUsecase,getStudentSubjectsScore:GetStudentSubjectsScoreUsecase) -> None:
        self._getStudentSubjects = getStudentSubjects
        self._getStudentSubjectsScore = getStudentSubjectsScore

    def __call__(self,req: HttpRequest) -> HttpResponse:
        if(type(req.query)['idStudent'] == None): return BadRequest('idStudent is null.')

        try:
            idStudent = req.query['idStudent']
            subjects = self._getStudentSubjects(idStudent=idStudent)            
            average = list(map(lambda x: AverageViewModel(media=randrange(0,100,5)/10,materia=x.name),subjects))
            response = AverageSubjectsViewModel(nomeGraduacao='Engenharia da Computação',ano=2022,medias=average)
            return Ok(response)
        except UnexpectedError as error:             
            return InternalServerError(error.args)