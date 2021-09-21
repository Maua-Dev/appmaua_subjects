from src.repositorios.mock.repositorio_materias_volatil_mock import MockRepositorioMateriasVolatil

def test_create_instance():
    repositorioMock = MockRepositorioMateriasVolatil()
    assert len(repositorioMock.materias) == 3