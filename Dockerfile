# Pull base image
FROM python:3.11.5-slim-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
# PIP_DISABLE_PIP_VERSION_CHECK turns off an automatic check for pip updates each time
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONDONTWRITEBYTECODE means Python will not try to write .pyc files
ENV PYTHONUNBUFFERED 1
# PYTHONUNBUFFERED ensures Docker does not buffer our console output

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements/base.txt .
RUN pip install -r base.txt

# Copy project
COPY library_api .