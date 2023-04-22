#!/bin/bash

docker build -t treasury-data-app-dev .
docker run -p 8501:8501 treasury-data-app-dev