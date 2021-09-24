class ErroGetAllMaterias(Exception):
    def __init__(self):
        super().__init__("Erro ao adquirir informacao das materias")