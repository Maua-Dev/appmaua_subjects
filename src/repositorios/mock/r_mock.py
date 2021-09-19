from src.interfaces.IRepo import IRepo


class RepoMock(IRepo):
    def __init__(self):
        pass

    def metodoRepo1(self):
        ret = 'Metodo repo 1 chamado'
        print(ret)
        return ret

    def metodoRepo2(self, arg):
        ret = f'Metodo repo 2 chamado e {arg=}'
        print(ret)
        return ret
