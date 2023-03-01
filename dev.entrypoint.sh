#!/bin/bash

RUN_PORT=${8000}

redis-server --daemonize yes
uvicorn src.api:app --host '0.0.0.0' --port ${RUN_PORT} --reload