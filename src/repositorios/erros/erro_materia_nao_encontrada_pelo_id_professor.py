class ErroMateriaNaoEncontradaPeloIDProfessor(Exception):
    def __init__(self, id: str):
        super().__init__(f"Não foram encontradas matérias para o professor de ID = {id}")