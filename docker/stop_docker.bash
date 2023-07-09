#!/bin/bash

SESSION=compose

tmux -2 new-session -d -s $SESSION

tmux new-window -t $SESSION:1 -n 'compose down'

tmux send-keys -t $SESSION:1 "cd \$MARRTINO_SOCIAL/docker && docker-compose down" C-m

tmux send-keys -t $SESSION:1 "docker container prune -f" C-m

