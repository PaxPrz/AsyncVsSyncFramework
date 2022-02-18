#! /bin/bash
# run with single worker
cd flaskapp
gunicorn -w 1 -b 127.0.0.1:8002 app:app
