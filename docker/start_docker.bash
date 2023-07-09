#!/bin/bash

docker-compose up
#SESSION=compose

#tmux -2 new-session -d -s $SESSION

#tmux rename-window -t $SESSION:0 'compose up'

#tmux send-keys -t $SESSION:0 "cd \$MARRTINO_SOCIAL/docker" C-m

#tmux send-keys -t $SESSION:0 "python3 dockerconfig.py " C-m
#sleep 1 # needed to complete writing /tmp/* files

#tmux send-keys -t $SESSION:0 "export ROBOT_TYPE=`cat /tmp/robottype` " C-m
#tmux send-keys -t $SESSION:0 "export CAMRES='`cat /tmp/cameraresolution`'" C-m

#tmux send-keys -t $SESSION:0 "docker-compose up" C-m


