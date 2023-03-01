#!/bin/bash

RUN_PORT=${PORT:-8000}

redis-server --daemonize yes
gunicorn -k uvicorn.workers.UvicornWorker src.api:app -b '0.0.0.0':${RUN_PORT}