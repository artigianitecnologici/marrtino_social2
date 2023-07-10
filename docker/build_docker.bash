#!/bin/bash
docker images -a | grep "noetic" | awk '{print $3}' | xargs docker rmi
docker build -t marrtino:noetic_system -f Dockerfile.noetic_system .
docker build -t marrtino:noetic_base -f Dockerfile.noetic_base .
docker build -t marrtino:noetic_oak-d -f Dockerfile.noetic_oak-d .
#docker build -t marrtino:social -f Dockerfile.noetic_social .
docker build -t marrtino:social -f Dockerfile.social .