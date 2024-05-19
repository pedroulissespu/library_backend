#!/bin/bash
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
COMPOSE_DIR="$SCRIPT_DIR/../compose"
cd "$COMPOSE_DIR" || exit
docker-compose -f local.yml down
