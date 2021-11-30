#!/bin/bash

# apps
rsync -avzr -e ssh \
    --progress \
    --exclude '*.pyc' \
    --exclude 'migrations' \
    --delete \
    apps/ \
    usuario@192.168.1.2:/home/usuario/django-lubre/apps

# static
rsync -avzr -e ssh \
    --progress \
    --exclude '*.pyc' \
    static/ \
    usuario@192.168.1.2:/home/usuario/django-lubre/static

# template
rsync -avzr -e ssh \
    --progress \
    --exclude '*.pyc' \
    --delete \
    templates/ \
    usuario@192.168.1.2:/home/usuario/django-lubre/templates
