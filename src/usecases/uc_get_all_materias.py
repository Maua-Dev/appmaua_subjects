from src.interfaces.i_getters_materias import IGettersMaterias
from src.repositorios.erros.erro_get_all_materias import ErroGetAllMaterias


class UCGetAllMaterias:
    repo: IGettersMaterias

    def __init__(self, repo: IGettersMaterias):
        self.repo = repo

    def __call__(self):
        try:
            materias = self.repo.getAllMaterias()
        except:
            raise ErroGetAllMaterias()

        return materias

