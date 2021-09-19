# Template para Fast API
[![codecov](https://codecov.io/gh/Maua-Dev/back_fastAPI_template/branch/main/graph/badge.svg?token=M16VBNGBR3)](https://codecov.io/gh/Maua-Dev/back_fastAPI_template)

Template de MSS para Fast API.

# Instalação

Comece ao clonar o repositório do modo que achar mais adequado.


### Criar um ambiente virtual python:
###### Windows:
    py -m venv venv
###### Linux:
    virtualenv -p python3.9 venv

### Ativar ambiente virtual:
###### Windows:
    venv\Scripts\activate
###### Linux:
    source venv/bin/activate

### Instalar pacotes necessários (ambos OS)
    pip install -r requirements.txt

# Uso:

### Desenvolvimento com Docker Composer

Para construir a imagem:

    docker-compose build

Para subir o container:

    docker-compose up


### Iniciar server
    uvicorn src.main:app --reload

### Rodar testes
    pytest

# Autores
## Grupo Backend (Ordem alfabetica):
    Bruna Galastri Guedes
    Bruno Vilardi Bueno
    Felipe Giusti
    Fernando Oliveira
    Nathan Brito da Silva
    Renan Reschke
    Vitor Martin

# Contribuições
Sendo um projeto fechado para alunos da faculdade Mauá, apenas os alunos podem contribuir para o projeto. 
Para mudanças, edições e outros, ver a seção de Issues e procurar a atividade designada a você.

# Licença
No momento, não há licença. 
