FROM python:3.11-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry
COPY pyproject.toml* poetry.lock* ./

COPY api api
COPY tests tests
COPY entrypoint.sh ./

RUN poetry config virtualenvs.in-project true
RUN if [-f pyproject.toml]; then poetry install --no-root; fi

ENTRYPOINT [ "bash", "entrypoint.sh" ]