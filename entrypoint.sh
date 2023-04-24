#!/bin/sh
systemctl restart nginx
gunicorn --bind :8000 --workers 3 portfolio.wsgi:application 
