FROM python:3.10-buster


RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt


WORKDIR /app
COPY . /app


EXPOSE 8080

CMD ["uvicorn", "spaceship.main:app", "--host", "0.0.0.0", "--port", "8080"]