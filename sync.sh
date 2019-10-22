#!/bin/bash

rsync -avzr -e ssh --progress --exclude '*.pyc' apps/      usuario@192.168.1.2:/home/usuario/django-lubre/apps
rsync -avzr -e ssh --progress --exclude '*.pyc' static/    usuario@192.168.1.2:/home/usuario/django-lubre/static
rsync -avzr -e ssh --progress --exclude '*.pyc' templates/ usuario@192.168.1.2:/home/usuario/django-lubre/templates

# no funciona
# rsync -avrP --include='*.{py,html}' --exclude='*.pyc' apps/ usuario@192.168.1.2:/home/usuario/django-lubre/apps

# rsync -avzr -e ssh --progress --include '*.py' --include '*.html' --exclude '*.pyc' apps/ usuario@192.168.1.2:/home/usuario/django-lubre/apps
