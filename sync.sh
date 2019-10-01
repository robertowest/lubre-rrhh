#!/bin/bash

# rsync -zvr apps/       usuario@192.168.1.2:/home/usuario/django-lubre/apps
# rsync -zvr static/     usuario@192.168.1.2:/home/usuario/django-lubre/static
# rsync -zvr templates/  usuario@192.168.1.2:/home/usuario/django-lubre/templates

rsync -avrP --include='*.'{py,html} --exclude='*' apps/ usuario@192.168.1.2:/home/usuario/django-lubre/apps
