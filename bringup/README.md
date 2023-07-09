# Bringup #

## Install ##

Install ```tmux```

    sudo apt install tmux


## Run

* Run the server

        python wsbringup.py

    You can check command execution with ```tmux a -t bringup```

## Web server

* Configure a web server to read <...>/marrtino_apps/www

* Open a browser at the URL

        http://<ROBOT_IP>/bringup

* Connect to the robot and control its running modules


## Start server at boot

Use script ```1-bringup.bash``` at init


## Bringup servers


wsbringup 9990 marrtino
wsbringup 9991 social

Run the bringup servers

        python robot_bringup.py -server_port 9236
        python vision_bringup.py -server_port 9237
        python nav_bringup.py -server_port 9238
        python speech_bringup.py -server_port 9239
        python teleop_bringup.py -server_port 9240
         
        python social_bringup.py -server_port 9250


Send commands to bringup servers

        echo '@robot' | netcat -w 1 localhost 9236
        echo '@robotkill' | netcat -w 1 localhost 9236
        echo '@orazioweb' | netcat -w 1 localhost 9236
        echo '@orazio2018web' | netcat -w 1 localhost 9236
        echo '@oraziowebkill' | netcat -w 1 localhost 9236
        echo '@firmware' | netcat -w 1 localhost 9236
        echo '@firmwareparams;[marrtino2019|pka03|ln298|arduino]' | netcat -w 1 localhost 9236

        echo '@usbcam' | netcat -w 1 localhost 9237
        echo '@astra' | netcat -w 1 localhost 9237
        echo '@xtion' | netcat -w 1 localhost 9237
        echo '@camerakill' | netcat -w 1 localhost 9237
        echo '@videoserver' | netcat -w 1 localhost 9237
        echo '@videoserverkill' | netcat -w 1 localhost 9237
        echo '@apriltags' | netcat -w 1 localhost 9237
        echo '@apriltagskill' | netcat -w 1 localhost 9237

        echo '@hokuyo' | netcat -w 1 localhost 9238
        echo '@rplidar' | netcat -w 1 localhost 9238
        echo '@laserkill' | netcat -w 1 localhost 9238
        echo '@loc' | netcat -w 1 localhost 9238
        echo '@lockill' | netcat -w 1 localhost 9238
        echo '@movebase' | netcat -w 1 localhost 9238
        echo '@movebasekill' | netcat -w 1 localhost 9238

        echo '@audio' | netcat -w 1 localhost 9239
        echo '@audiokill' | netcat -w 1 localhost 9239

        echo '@joystick' | netcat -w 1 localhost 9240
        echo '@joystick4wd' | netcat -w 1 localhost 9240
        echo '@joystickkill' | netcat -w 1 localhost 9240

