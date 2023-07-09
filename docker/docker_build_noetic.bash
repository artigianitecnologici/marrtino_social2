#!/bin/bash
docker build -t marrtino:noetic_system -f Dockerfile.noetic_system .
docker build -t marrtino:noetic_base -f Dockerfile.noetic_base .
docker build -t marrtino:noetic_oak-d -f Dockerfile.noetic_oak-d .