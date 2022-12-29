#!/bin/bash

RUN_PORT=${PORT:-8000}

uvicorn src.api:app --host '0.0.0.0' --port ${RUN_PORT} --reload