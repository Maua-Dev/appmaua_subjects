# from src.interfaces.IRepoMaterias import IRepoMaterias
# from src.repositorios.erros.erro_materia_nao_encontrada_pelo_id_professor import ErroMateriaNaoEncontradaPeloIDProfessor


# class UCGetMateriaPorIDProfessor:
#     repo: IRepoMaterias

#     def __init__(self, repo: IRepoMaterias):
#         self.repo = repo

#     def __call__(self, id: str):
#         try:
#             materias = self.repo.getMateriaPorIDProfessor(id)
#             if len(materias) == 0 :
#                 raise ErroMateriaNaoEncontradaPeloIDProfessor(id)
#         except Exception:
#             raise ErroMateriaNaoEncontradaPeloIDProfessor(id)

#         return materias
