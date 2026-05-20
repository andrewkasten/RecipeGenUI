#!/usr/bin/env bash
set -euo pipefail

# -p genui isolates this stack from any other compose project (e.g. ImpactDesk)
# running on the same host — containers, networks, and the postgres volume
# get a "genui_" prefix.
COMPOSE="docker compose -p genui -f docker-compose.prod.yml"

# Ensure the host directory the (ImpactDesk-side) nginx will serve from exists
# and is writable by the build container.
sudo mkdir -p /opt/genui/dist
sudo chown "$USER":"$USER" /opt/genui/dist

# Build the api image, then run the one-shot frontend builder to populate
# /opt/genui/dist with the compiled React app.
$COMPOSE build api
$COMPOSE run --rm frontend-build

# Bring up the long-running services.
$COMPOSE up -d db api

# Wait for db to accept connections, then migrate.
sleep 5
$COMPOSE exec -T api python manage.py migrate
