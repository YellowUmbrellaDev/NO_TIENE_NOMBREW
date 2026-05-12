#!/bin/sh
git config --global --add safe.directory /srv
cd /srv

if [ ! -d ".git" ]; then
    # Primera vez: el volumen está vacío, clonamos el repositorio
    git clone git@github.com:YellowUmbrellaDev/NO_TIENE_NOMBREW.git .
else
    # Siguientes veces: forzamos sincronización exacta con el remoto
    git fetch git@github.com:YellowUmbrellaDev/NO_TIENE_NOMBREW.git master
    git reset --hard FETCH_HEAD
fi
