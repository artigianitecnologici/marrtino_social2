#!/bin/bash
docker images -a | grep "noetic" | awk '{print $3}' | xargs docker rmi
docker images -a | grep "orazio" | awk '{print $3}' | xargs docker rmi
docker images -a | grep "social" | awk '{print $3}' | xargs docker rmi
# prune 
docker container prune -f
docker image prune -f
docker builder prune 

