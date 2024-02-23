#!/bin/sh

docker compose up -d

# launching container with python application
docker compose exec -it pythonapp bash
