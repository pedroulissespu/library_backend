#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
COMPOSE_DIR="$SCRIPT_DIR/../compose"
cd "$COMPOSE_DIR" || exit
docker-compose -f local.yml exec web python manage.py loaddata library/authors/fixtures/authors.json
docker-compose -f local.yml exec web python manage.py loaddata library/books/fixtures/books.json
