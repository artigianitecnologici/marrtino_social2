#!/bin/bash

set -e
set -x

docker build --no-cache --build-arg KALDI_MKL=0 --file Dockerfile.kaldi-vosk-server --tag alphacep/kaldi-vosk-server:latest .
docker build --file Dockerfile.kaldi-it --tag alphacep/kaldi-it:latest .
docker build -t marrtino:vosk-client -f Dockerfile.vosk-client .