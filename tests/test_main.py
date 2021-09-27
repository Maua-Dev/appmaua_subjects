from fastapi.testclient import TestClient
from fastapi import status

from src.controladores.fastapi.http.respostas import ResRoot
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import *
from src.main import main

(_, ctrl) = main()
client = TestClient(ctrl.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == ResRoot(deployment=ProjConfig.getDeployment(), controlador=ProjConfig.getFastapi())


def test_read_materias():
    resposta = client.get("/materias")
    assert resposta.status_code == status.HTTP_200_OK

def test_read_materias_id_existe():
    resposta = client.get("/materias/ecm251")
    assert resposta.status_code == status.HTTP_200_OK

def test_read_materias_id_nao_existe():
    resposta = client.get("/materias/esm250")
    assert resposta.status_code == status.HTTP_404_NOT_FOUND