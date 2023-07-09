#!/bin/bash

source $MARRTINO_SOCIAL2/docker/stop_docker.bash 

sleep 5

cd $MARRTINO_SOCIAL2/docker
git pull
#python3 dockerconfig.py
docker-compose pull
docker build -t marrtino:social -f Dockerfile.system .
docker-compose build
cd -

docker container prune -f
docker image prune -f

date > ~/log/last_systemupdate

source $MARRTINO_SOCIAL2/docker/start_docker.bash

