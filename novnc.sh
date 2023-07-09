#!/bin/sh
echo "Launch NOVNC"

echo "installation -------------------"
echo "sudo apt install -y novnc x11vnc"
echo "--------------------------------" 
# ------------------------------------
x11vnc -display :0 -autoport -localhost -nopw -bg -xkb -ncache -ncache_cr -quiet -forever
/usr/share/novnc/utils/launch.sh --listen 8085 --vnc localhost:5900