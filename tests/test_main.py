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
    assert resposta.json() == {"repo": {"materias": [
        {"codigo": "Linguagens de Programação I", "tipo": 2, "semestralidade": 3,
         "profOrientador": {"nome": "Jorge Do Teste",
                            "contato": {"telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                                        "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}],
                                        "enderecos": [{"logradouro": "rua de tal", "numero": 20, "cep": "00000-000",
                                                       "complemento": None, "tipo": 1}]}, "nascimento": "1999-02-23",
                            "roles": [2], "timestamp": None, "ID": "0002", "troncos": ["Eletrica"],
                            "cursos": ["Engenharia de Computação"], "disciplinas": ["Linguagens de Programação I"]},
         "professores": [{"nome": "Jorge Do Teste",
                          "contato": {"telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                                      "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}],
                                      "enderecos": [{"logradouro": "rua de tal", "numero": 20, "cep": "00000-000",
                                                     "complemento": None, "tipo": 1}]}, "nascimento": "1999-02-23",
                          "roles": [2], "timestamp": None, "ID": "0002", "troncos": ["Eletrica"],
                          "cursos": ["Engenharia de Computação"], "disciplinas": ["Linguagens de Programação I"]}],
         "alunosMatriculados": [{"nome": "Jorge Do Teste", "contato": {
             "telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
             "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}], "enderecos": [
                 {"logradouro": "rua de tal", "numero": 20, "cep": "00000-000", "complemento": None, "tipo": 1}]},
                                 "nascimento": "1999-02-23", "roles": [9], "timestamp": None,
                                 "ra": {"ano": "19", "numero": "02009", "digito": "0"},
                                 "curso": "Engenharia de Computação", "serie": 3,
                                 "disciplinas": ["Linguagens de Programação I"], "periodo": "Diurno", "listaDPs": [],
                                 "hasDP": False}], "aulas": [{"disciplina": "Linguagens de Programação I",
                                                              "local": {"bloco": "U", "numeroDaSala": 22, "tipo": [1],
                                                                        "campus": "São Caetano do Sul"},
                                                              "horario": "2021-07-12T07:40:00", "duracao": "01:40:00",
                                                              "professor": {"nome": "Jorge Do Teste", "contato": {
                                                                  "telefones": [
                                                                      {"tipo": 2, "numero": "99999-9999", "ddd": 11,
                                                                       "prioridade": 3}], "emails": [
                                                                      {"email": "teste@teste.com", "tipo": 1,
                                                                       "prioridade": 1}], "enderecos": [
                                                                      {"logradouro": "rua de tal", "numero": 20,
                                                                       "cep": "00000-000", "complemento": None,
                                                                       "tipo": 1}]}, "nascimento": "1999-02-23",
                                                                            "roles": [2], "timestamp": None,
                                                                            "ID": "0002", "troncos": ["Eletrica"],
                                                                            "cursos": ["Engenharia de Computação"],
                                                                            "disciplinas": [
                                                                                "Linguagens de Programação I"]}}],
         "ofereceDp": True}, {"codigo": "Linguagens de Programação I", "tipo": 3, "semestralidade": 1,
                              "profOrientador": {"nome": "Jorge Do Teste", "contato": {
                                  "telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                                  "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}], "enderecos": [
                                      {"logradouro": "rua de tal", "numero": 20, "cep": "00000-000",
                                       "complemento": None, "tipo": 1}]}, "nascimento": "1999-02-23", "roles": [2],
                                                 "timestamp": None, "ID": "0002", "troncos": ["Eletrica"],
                                                 "cursos": ["Engenharia de Computação"],
                                                 "disciplinas": ["Linguagens de Programação I"]}, "professores": [
                {"nome": "Jorge Do Teste",
                 "contato": {"telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                             "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}], "enderecos": [
                         {"logradouro": "rua de tal", "numero": 20, "cep": "00000-000", "complemento": None,
                          "tipo": 1}]}, "nascimento": "1999-02-23", "roles": [2], "timestamp": None, "ID": "0002",
                 "troncos": ["Eletrica"], "cursos": ["Engenharia de Computação"],
                 "disciplinas": ["Linguagens de Programação I"]}], "alunosMatriculados": [{"nome": "Jorge Do Teste",
                                                                                           "contato": {"telefones": [
                                                                                               {"tipo": 2,
                                                                                                "numero": "99999-9999",
                                                                                                "ddd": 11,
                                                                                                "prioridade": 3}],
                                                                                               "emails": [{
                                                                                                   "email":
                                                                                                       "teste@teste.com",
                                                                                                   "tipo": 1,
                                                                                                   "prioridade": 1}],
                                                                                               "enderecos": [{
                                                                                                   "logradouro": "rua "
                                                                                                                 "de "
                                                                                                                 "tal",
                                                                                                   "numero": 20,
                                                                                                   "cep": "00000-000",
                                                                                                   "complemento": None,
                                                                                                   "tipo": 1}]},
                                                                                           "nascimento": "1999-02-23",
                                                                                           "roles": [9],
                                                                                           "timestamp": None,
                                                                                           "ra": {"ano": "19",
                                                                                                  "numero": "02009",
                                                                                                  "digito": "0"},
                                                                                           "curso": "Engenharia de "
                                                                                                    "Computação",
                                                                                           "serie": 3, "disciplinas": [
                    "Linguagens de Programação I"], "periodo": "Diurno", "listaDPs": [], "hasDP": False}], "aulas": [
                {"disciplina": "Linguagens de Programação I",
                 "local": {"bloco": "U", "numeroDaSala": 22, "tipo": [1], "campus": "São Caetano do Sul"},
                 "horario": "2021-07-12T07:40:00", "duracao": "01:40:00", "professor": {"nome": "Jorge Do Teste",
                                                                                        "contato": {"telefones": [
                                                                                            {"tipo": 2,
                                                                                             "numero": "99999-9999",
                                                                                             "ddd": 11,
                                                                                             "prioridade": 3}],
                                                                                            "emails": [{
                                                                                                "email":
                                                                                                    "teste@teste.com",
                                                                                                "tipo": 1,
                                                                                                "prioridade": 1}],
                                                                                            "enderecos": [{
                                                                                                "logradouro": "rua de "
                                                                                                              "tal",
                                                                                                "numero": 20,
                                                                                                "cep": "00000-000",
                                                                                                "complemento": None,
                                                                                                "tipo": 1}]},
                                                                                        "nascimento": "1999-02-23",
                                                                                        "roles": [2], "timestamp": None,
                                                                                        "ID": "0002",
                                                                                        "troncos": ["Eletrica"],
                                                                                        "cursos": [
                                                                                            "Engenharia de Computação"],
                                                                                        "disciplinas": [
                                                                                            "Linguagens de "
                                                                                            "Programação I"]}}],
                              "ofereceDp": True},
        {"codigo": "Linguagens de Programação I", "tipo": 1, "semestralidade": 2,
         "profOrientador": {"nome": "Jorge Do Teste",
                            "contato": {"telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                                        "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}],
                                        "enderecos": [{"logradouro": "rua de tal", "numero": 20, "cep": "00000-000",
                                                       "complemento": None, "tipo": 1}]}, "nascimento": "1999-02-23",
                            "roles": [2], "timestamp": None, "ID": "0002", "troncos": ["Eletrica"],
                            "cursos": ["Engenharia de Computação"], "disciplinas": ["Linguagens de Programação I"]},
         "professores": [{"nome": "Jorge Do Teste",
                          "contato": {"telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
                                      "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}],
                                      "enderecos": [{"logradouro": "rua de tal", "numero": 20, "cep": "00000-000",
                                                     "complemento": None, "tipo": 1}]}, "nascimento": "1999-02-23",
                          "roles": [2], "timestamp": None, "ID": "0002", "troncos": ["Eletrica"],
                          "cursos": ["Engenharia de Computação"], "disciplinas": ["Linguagens de Programação I"]}],
         "alunosMatriculados": [{"nome": "Jorge Do Teste", "contato": {
             "telefones": [{"tipo": 2, "numero": "99999-9999", "ddd": 11, "prioridade": 3}],
             "emails": [{"email": "teste@teste.com", "tipo": 1, "prioridade": 1}], "enderecos": [
                 {"logradouro": "rua de tal", "numero": 20, "cep": "00000-000", "complemento": None, "tipo": 1}]},
                                 "nascimento": "1999-02-23", "roles": [9], "timestamp": None,
                                 "ra": {"ano": "19", "numero": "02009", "digito": "0"},
                                 "curso": "Engenharia de Computação", "serie": 3,
                                 "disciplinas": ["Linguagens de Programação I"], "periodo": "Diurno", "listaDPs": [],
                                 "hasDP": False}], "aulas": [{"disciplina": "Linguagens de Programação I",
                                                              "local": {"bloco": "U", "numeroDaSala": 22, "tipo": [1],
                                                                        "campus": "São Caetano do Sul"},
                                                              "horario": "2021-07-12T07:40:00", "duracao": "01:40:00",
                                                              "professor": {"nome": "Jorge Do Teste", "contato": {
                                                                  "telefones": [
                                                                      {"tipo": 2, "numero": "99999-9999", "ddd": 11,
                                                                       "prioridade": 3}], "emails": [
                                                                      {"email": "teste@teste.com", "tipo": 1,
                                                                       "prioridade": 1}], "enderecos": [
                                                                      {"logradouro": "rua de tal", "numero": 20,
                                                                       "cep": "00000-000", "complemento": None,
                                                                       "tipo": 1}]}, "nascimento": "1999-02-23",
                                                                            "roles": [2], "timestamp": None,
                                                                            "ID": "0002", "troncos": ["Eletrica"],
                                                                            "cursos": ["Engenharia de Computação"],
                                                                            "disciplinas": [
                                                                                "Linguagens de Programação I"]}}],
         "ofereceDp": True}]}}
