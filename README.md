# marrtino_social

# NOVNC Installation
## 
   sudo apt install x11vnc
## 
   /usr/share/novnc/utils/launch.sh --listen 8084 --vnc localhost:5900


# config env

    
    export MARRTINO_APPS_HOME=$HOME/src/marrtino_apps
    #export MARRTINO_APPS_HOME2=$HOME/src/marrtino_apps2
    export MARRTINO_SOCIAL=$HOME/src/marrtino_social2
    export MARRTINO_SOCIAL2=$HOME/src/marrtino_social2

    export ROS_IP=127.0.0.1
    #export ROS_IP=192.168.1.86
    export ROBOT_TYPE=marrtino

    # check if session already exists
    tmux has-session -t compose 2>/dev/null
    export UID=$(id -u)
    export GID=$(id -g)
    # check if session already exists
    tmux has-session -t compose 2>/dev/null
    #Alias
    alias cw='cd ~/ros/catkin_ws'
    alias cds='cd ~/src/marrtino_social2'
    alias cda='cd ~/src/marrtino_apps' 
    alias cdsd='cd ~/src/marrtino_social2/docker'
    alias cdad='cd ~/src/marrtino_apps/docker'
    alias cm='cd ~/src/catkin_ws && catkin_make'

# Docker images

## Pre requisites

sudo apt install chromium-browser


Follow instructions for installing and using [marrtino_apps](https://bitbucket.org/iocchi/marrtino_apps/src/master/docker)


## Configuration

Enable the `social` feature in `system_config.yaml`

        nano system_config.yaml

            ...

            functions:
              ...
              social: on



## Update and build

        cd $MARRTINO_APPS_HOME2/docker
        ./system_update.bash

## Run

        cd $MARRTINO_APPS_HOME2/docker
        ./start_docker.bash

## Quit

        cd <...>/marrtino_apps/docker
        ./stop_docker.bash


## Bringup servers

To interact with docker containers, see 
[bringup/README](https://bitbucket.org/iocchi/marrtino_apps/src/master/bringup/README.md)

## Docker access

        docker exec -it <container_name> tmux a
        docker exec 5de4af7d973a tmux a
        docker exec -it social tmux a


## Docker push

    Edit `Dockerfile.<component>` setting last docker build date

        RUN echo "<date>" > /tmp/lastdockerbuild


    Commit ang push last changes

        git commit -am "dockerhub <date>"
        git push



    Push on Docker hub (you may need to change the docker tags)

        ./docker_build.bash
        ./docker_push.bash


## Command line instructions to manage MARRtina display

Set display (if connected through ssh)

    export DISPLAY=:0

Rotation

    xrandr -o <normal,inverted,left,right,0,1,2,3>

Launch MARRtina face

    firefox --safe-mode --kiosk localhost:8080/social/marrtina.html

Go fullscreen
    
    xdotool search --sync --onlyvisible --class "Firefox" windowactivate key F11

Refresh page (e.g., after restarting social node)

    xdotool search --sync --onlyvisible --class "Firefox" windowactivate key F5

Kill firefox page

    xdotool search --sync --onlyvisible --class "Firefox" windowkill


Remove warning windows in firefox (use a remote connection `ssh -Y marrtino@10.3.1.1` to launch firefox on remote desktop)

    enter about:config into the firefox address bar (confirm the info message in case it shows up) 
    search for the preference named browser.sessionstore.resume_from_crash change its value to false


Remove screen saver

    sudo gsettings set org.gnome.desktop.screensaver lock-delay 0
    sudo gsettings set org.gnome.desktop.screensaver lock-enabled false
    sudo gsettings set org.gnome.desktop.screensaver idle-activation-enabled false


sudo chown -R www-data:www-data tmp

sudo chown -R $USER:$USER tmp
