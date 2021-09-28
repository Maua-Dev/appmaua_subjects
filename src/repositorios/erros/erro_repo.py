class ErroRepo(Exception):
    def __init__(self):
        super().__init__("Erro de repositório")
