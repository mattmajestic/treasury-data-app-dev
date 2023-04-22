#!/bin/bash

docker build -t treasury-data-api-dev .
docker run -p 8000:8000 treasury-data-api-dev