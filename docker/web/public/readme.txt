*
* README.txt
*
* PREREQUISITI
* =========================================================
* INSTALLAZIONE ROSBRIDGE SERVER
* =========================================================
sudo apt-get install ros-melodic-rosbridge-server
rosdep install rosbridge_server
sudo apt-get install ros-melodic-rosbridge-suite
source /opt/ros/melodic/setup.bash

web_video_server
* =========================================================
* INSTALLAZIONE DYNAMIXEL 
* =========================================================




find_dinamyxel.sh -- Cerca I servo Dynamixel Collegati
* =========================================================
* CONFIGURAZIONE PAN 
* =========================================================
sudo apt-get install ros-melodic-usb-cam ros-melodic-image-view ros-melodic-cv-bridge
face_tracker_control/config/pan.yaml
* =========================================================
* CREAZIONE SYMBOLIC LINK
* =========================================================
ln -s $HOME/src/MARRtinoSocial/www/social  /var/www/html/marrtino/social
