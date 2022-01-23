FROM python:3.9.6-alpine

WORKDIR /app
RUN apk update
RUN apk add git
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install uvicorn

EXPOSE 8000

COPY . /app

CMD ["uvicorn", "src.server:app", "--reload", "--host", "0.0.0.0"] 