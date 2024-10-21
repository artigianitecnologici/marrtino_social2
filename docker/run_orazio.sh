#!/bin/bash 

IMAGENAME=marrtino:noetic_orazio
# change setings here if needed
#if [ "$ROBOT_IP" == "" ]; then
  echo "Set ROBOT_IP env var to IP of robot running roscore"
  #export ROBOT_IP=127.0.0.1
  export ROS_IP=10.3.1.1
  #exit 1
#fi

echo "Running image $IMAGENAME ..."

docker run -it \
    --name marrtinonoeticorazio --rm \
    -v /dev/:/dev/ \
    -v $HOME/src/marrtino_social2/script:/home/robot/script \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -v $HOME/.Xauthority:/home/robot/.Xauthority:rw \
    -e DISPLAY=$DISPLAY \
    -e ROS_IP=$ROS_IP \
    -e ROS_MASTER_URI=http://$ROBOT_IP:11311 \
    --privileged \
    --net=host \
    -v $MARRTINO_PLAYGROUND:/home/robot/playground \
    -v $MARRTINO_APPS_HOME:/home/robot/src/marrtino_apps \
    $IMAGENAME \
    tmux

