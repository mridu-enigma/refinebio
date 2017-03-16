#!/bin/bash

# convenience script for running the worker docker container

HOST_IP=$(ifconfig eth0 | grep "inet " | awk -F'[: ]+' '{ print $4 }')
docker run \
       --link some-rabbit:rabbit \
       --name worker1 \
       --add-host=database:$HOST_IP \
       --env-file workers/environments/dev \
       -d bm_worker
