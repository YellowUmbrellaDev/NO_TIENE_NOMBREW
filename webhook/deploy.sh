#!/bin/sh
git config --global --add safe.directory /srv
cd /srv
git remote set-url origin https://github.com/YellowUmbrellaDev/NO_TIENE_NOMBREW.git
git pull origin master
docker compose up -d
