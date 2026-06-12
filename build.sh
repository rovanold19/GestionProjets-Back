#!/usr/bin/env bash
# Arrête le script au moindre problème
set -o errexit

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques et appliquer les migrations PostgreSQL
python manage.py collectstatic --no-input
python manage.py migrate
