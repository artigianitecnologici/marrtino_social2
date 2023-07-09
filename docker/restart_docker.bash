#!/bin/bash

source $MARRTINO_APPS_HOME/docker/stop_docker.bash 

sleep 5

DPS=`docker ps | wc -l`
while (( $DPS > 1 )) ; do
  sleep 3
  DPS=` docker ps | wc -l`
done

source $MARRTINO_APPS_HOME/docker/start_docker.bash

DPS=`docker ps | wc -l`
while (( $DPS == 1 )) ; do
  sleep 3
  DPS=`docker ps | wc -l`
done

echo "Done"

