class ErroGetAllMaterias(Exception):
    def __init__(self):
        super().__init__("Erro ao adquirir informação das matérias")