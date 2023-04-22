#!/bin/bash

echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker build -t ghcr.io/mattmajestic/treasury-data-api-dev:latest .
docker push ghcr.io/mattmajestic/treasury-data-api-dev:latest