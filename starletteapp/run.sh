#! /bin/bash
# run with single worker
cd starletteapp
gunicorn -w 1 -k uvicorn.workers.UvicornWorker -b 127.0.0.1:8001 app:app
