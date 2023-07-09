#!/bin/bash

# launched by marrtino:base container

date

if [ "$MARRTINO_APPS_HOME2" == "" ]; then
  export MARRTINO_APPS_HOME=$HOME/src/marrtino_apps
fi

if [ "$MODIM_HOME" == "" ]; then
  export MODIM_HOME=$HOME/src/modim
fi

if [ "$MARRTINO_SOCIAL2" == "" ]; then
  export MARRTINO_SOCIAL2=$HOME/src/marrtino_social
fi

#source $HOME/.bashrc
source $HOME/ros/catkin_ws/devel/setup.bash
#export DISPLAY=:0
#export ROBOT_TYPE=marrtino

mkdir -p $HOME/log

SESSION=init

# check if session already exists
tmux has-session -t $SESSION 2>/dev/null

if [ $? != 0 ]; then
  # Set up your session
  tmux -2 new-session -d -s $SESSION
  tmux new-window -t $SESSION:0 -n 'bringup'
  tmux new-window -t $SESSION:1 -n 'wsrobot'
fi



tmux send-keys -t $SESSION:0 "cd \$MARRTINO_SOCIAL2/bringup" C-m
tmux send-keys -t $SESSION:0 "python social_bringup.py" C-m


#tmux send-keys -t $SESSION:1 "cd \$MARRTINO_SOCIAL2/docker/web/public/program/blockly" C-m
#tmux send-keys -t $SESSION:1 "python websocket_robot.py" C-m



while [ ! -f "/tmp/quitrequest" ]; do
  sleep 5
done

