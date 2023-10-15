FROM python:3.11.6-slim-bookworm

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    DISABLE_POETRY_CREATE_RUNTIME_FILE=1 \
    PYTHON_RUNTIME_VERSION=3.11.6

RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install "poetry==$POETRY_VERSION"

RUN mkdir -p /app/
WORKDIR /app/

COPY pyproject.toml poetry.lock* ./docker/app-entrypoint.sh /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY app/ /app/

ENTRYPOINT ["./app-entrypoint.sh"]
