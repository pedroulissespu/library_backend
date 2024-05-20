#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
COMPOSE_DIR="$SCRIPT_DIR/../compose"
cd "$COMPOSE_DIR" || exit
docker-compose -f postgres.yml up -d --build
PYTHON_MANAGE_DIR="$SCRIPT_DIR/.."
cd "$PYTHON_MANAGE_DIR" || exit
python manage.py makemigrations
python manage.py migrate
cd "$COMPOSE_DIR" || exit
docker-compose -f postgres.yml down
