class ErroMateriaNaoEncontrada(Exception):
    def __init__(self):
        super().__init__("A matéria requisitada não foi encontrada")