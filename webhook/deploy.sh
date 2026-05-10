#!/bin/sh
# Configura git para que no se queje de los permisos del host vs contenedor
git config --global --add safe.directory /srv
cd /srv
# Descarga los ultimos cambios de github
git pull origin main
# Reinicia los contenedores (este comando envia la orden al host via docker.sock)
docker compose up -d
