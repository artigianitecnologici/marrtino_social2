#!/bin/bash

docker tag marrtino:base iocchi/marrtino:base
docker tag marrtino:teleop iocchi/marrtino:teleop
docker tag marrtino:navigation iocchi/marrtino:navigation
docker tag marrtino:vision iocchi/marrtino:vision
docker tag marrtino:speech iocchi/marrtino:speech

docker login

docker push iocchi/marrtino:base && \
docker push iocchi/marrtino:teleop && \
docker push iocchi/marrtino:navigation && \
docker push iocchi/marrtino:vision && \
docker push iocchi/marrtino:speech



