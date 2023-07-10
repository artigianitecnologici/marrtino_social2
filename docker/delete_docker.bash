#!/bin/bash
docker images -a | grep "noetic" | awk '{print $3}' | xargs docker rmi
