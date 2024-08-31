FROM python:3.12

RUN mkdir /code

WORKDIR /code

#COPY requirements.txt .
COPY pyproject.toml .
COPY poetry.lock .

RUN pip install poetry
RUN poetry install
# RUN pip install -r requirements.txt

COPY . .

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8080"]