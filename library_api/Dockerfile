# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY requirements/base.txt .

RUN python -m venv /opt/venv

RUN /opt/venv/bin/pip install --upgrade pip && \
    /opt/venv/bin/pip install --no-cache-dir -r base.txt

ENV PATH="/opt/venv/bin:$PATH"

COPY . .

CMD ["gunicorn", "--bind", ":8000", "library_api.wsgi:application"]