FROM python:3.10-buster

RUN apt-get update && apt-get install python-mysqldb

COPY . /code/application/

RUN pip install -r /code/application/requirements.txt

EXPOSE 8080

WORKDIR /code
CMD ["python3", "-m", "application"]