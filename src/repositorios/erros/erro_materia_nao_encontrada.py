class ErroMateriaNaoEncontrada(Exception):
    def __init__(self):
        super().__init__("A materia requisitada nao foi encontrada")