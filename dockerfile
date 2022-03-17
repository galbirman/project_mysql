FROM python:3.9

WORKDIR /project

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

ADD . /project

CMD ["python","app.py"]
