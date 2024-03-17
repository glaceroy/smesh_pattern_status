FROM python:alpine3.19

RUN pip install --upgrade pip

RUN adduser -D flaskuser

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

USER flaskuser

CMD ["python3", "main.py"]