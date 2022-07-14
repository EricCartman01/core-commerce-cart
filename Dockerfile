# Builder
FROM python:3.9.8-slim-buster AS python-builder

WORKDIR /app

ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install poetry

COPY poetry.lock pyproject.toml /app/
COPY src/ /app/src

RUN poetry config virtualenvs.in-project true
RUN poetry install --no-dev


# Base app
FROM python:3.9.8-slim-buster AS app-base

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"
ENV LANG=C.UTF-8
ENV PYTHONUNBUFFERED=1

COPY --from=python-builder /app /app


# For development
FROM app-base AS devapp

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY tests/ /app/tests/
COPY .coveragerc /app/

RUN pip install poetry
RUN poetry config virtualenvs.in-project true
RUN poetry install


# For deployment
FROM app-base AS release
