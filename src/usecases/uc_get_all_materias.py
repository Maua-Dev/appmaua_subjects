from src.interfaces.IRepoMaterias import IRepoMaterias
from src.repositorios.erros.erro_get_all_materias import ErroGetAllMaterias


class UCGetAllMaterias:
    repo: IRepoMaterias

    def __init__(self, repo: IRepoMaterias):
        self.repo = repo

    def __call__(self):
        try:
            materias = self.repo.getAllMaterias()
        except:
            raise ErroGetAllMaterias

        return materias

