#!/bin/bash

RUN_PORT=${PORT:-8000}

redis-server /etc/redis/6379.conf
uvicorn src.api:app --host '0.0.0.0' --port ${RUN_PORT} --reload