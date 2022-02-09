from src.adapters.controllers.get_student_subjects_controller import GetStudentSubjectsController
from src.main.subjects.module import Module,Modular


class Test_Module:

    def test_module_working(self):
        controller = Modular.getInject(GetStudentSubjectsController)
        assert isinstance(controller,GetStudentSubjectsController)