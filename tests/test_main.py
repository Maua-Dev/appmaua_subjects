from fastapi.testclient import TestClient

from src.controladores.fastapi.http.respostas import ResRoot
from src.fabricas.controladores.fastapi.fabrica_controlador_fastapi import *
from src.main import main

(_, ctrl) = main()
client = TestClient(ctrl.app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == ResRoot(deployment=ProjConfig.getDeployment(), controlador=ProjConfig.getFastapi())


def test_read_materias():
    resposta = client.get("/materias")
    assert resposta.status_code == 200

def test_read_materias_id_existe():
    resposta = client.get("/materias/esm251")
    assert resposta.status_code == 200

def test_read_materias_id_nao_existe():
    resposta = client.get("/materias/esm250")
    assert resposta.status_code == 200