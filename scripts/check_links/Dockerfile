FROM python:3.9-slim 

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True
ENV ENV_NAME=staging

WORKDIR /app

RUN pip3 install poetry
RUN poetry config virtualenvs.create false

# add and install python requirements
COPY pyproject.toml ./
COPY poetry.lock ./
RUN poetry install --no-dev

COPY . ./

CMD ["poetry", "run", "python", "main.py"]
