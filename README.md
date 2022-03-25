# Template para Fast API
[![codecov](https://codecov.io/gh/Maua-Dev/mss_materias/branch/main/graph/badge.svg?token=NIRZLES7VB)](https://codecov.io/gh/Maua-Dev/mss_materias)

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

### Subir um container PostgreSQL
##### 1. Obter a imagem do Postgres
    docker pull postgres
##### 2. Criar um container
    docker run --name devmaua_postgres -p 5432:5432 -e POSTGRES_PASSWORD=devmaua -d postgres
##### 3. Conectar ao postgres
    docker exec -it devmaua_postgres psql -U postgres -W
    (senha = devmaua)
##### 4. Criar o database "Devmaua"
    create database "Devmaua";
##### 5. Fechar o cmd
##### 6. Criar um .bat com o comando:
    docker exec -it devmaua_postgres psql -U postgres -W -d Devmaua
Ao executar esse .bat você se conectará automaticamente ao banco (basta inserir a senha "devmaua").
Obs: o nome do container "devmaua_postgres" pode ser mudado para o que preferir.



### Iniciar server
    uvicorn src.main.main:app --reload

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
