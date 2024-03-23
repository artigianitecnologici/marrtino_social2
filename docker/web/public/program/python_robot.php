<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>Python robot</title>

  <!-- CSS  -->
  <link href="../css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="../css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <!--<script src="js/jquery-3.4.1.min.js"></script>-->
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <script src="websocket_robot.js"></script>  
</head>
<body>

<?php include "../social/nav.php" ?>


  <h1 align="center">Python robot</h1>

  <div class="container">

  <p>Executing Python programs on robot.</p>

  <p>
    <table>
    <tr height=40 style="border:none">
      <td>Robot IP</td>
<script>
      document.write("<td><input type=\"text\" name=\"IP\" id=\"IP\" value=\"" + 
            window.location.hostname + "\" width=240></td>")
</script>
      <tr style="border:none">
      <td></td>
      <td>
		<button onclick="connect()" class="btn waves-effect waves-light blue" style="margin-right:10px">Connect</button>
		<button onclick="disconnect()" class="btn waves-effect waves-light blue" style="margin-right:10px">Disconnect</button>
	  </td>	  
    </tr>
	<tr>
		<td></td>
		<td>
			<div id="connection"><font color='red'>Not Connected</font></div>
		</td>
	</tr>
    <tr>
      <td>Status</td>
      <td><div id="status" style="color: blue;" >Idle</div></td>
    </tr>
    </table>
  </p>

  <br>

  <p>
    <button id="run_btn" onclick="runCode()" class="btn waves-effect waves-light blue" style="margin-right:10px">Run</button>
    <button id="stop_btn" onclick="stopCode()" class="btn waves-effect waves-light blue">Stop</button>
  </p>

  <table border=0>
  <tr>  <th>Python workspace</th>  </tr>
  <tr>
  <td>
    <div>
<textarea id="code" rows=20 cols=60 style="height:400px"># Write your robot program here


</textarea>
    </div>
    
  </td>
  </tr>
  </table>

<br>

  <table border=0>
  <tr>  <th>Display</th>  </tr>
  <tr>
  <td style="color:#0000FF; background-color: #EEFFCC; font-size: 150%;" width=500 height=50>
    <div id="display">
    </div>    
  </td>
  </tr>
  </table>


  <table border=0>
  <tr>  <th>Image</th>  </tr>
  <tr>
  <td width=500 height=50 bgcolor=#B0CFB0>
    <div align='center' > <img height=300 id='image' src="../viewer/img/lastimage.jpg" alt=""/> </div>
  </td>
  </tr>
  </table>

<br><br>


<hr>

<h3>Commands</h3>

<listing style="font-size:125%;">

textsay = wait_user_speaking( sec )
result = ask_chatgpt( textsay)
say(result)

# motion

enableObstacleAvoidance(False|True) 
forward(m)
backward(m)
left(n)
right(n)
turn(deg, ref='REL'|'ABS', frame='odom'|'map'):
setSpeed(lx,az,tm,stopend=False)
setSpeed4W(fl,fr,bl,br,tm,stopend=False)
stop()
goto(gx,gy,gth)     # map pose (move_base)
gotoLabel(label)    # semantic map (map_server, move_base)
gotoTarget(gx,gy, frame='odom'|'map'|'gt')  # no path planning
p = getRobotPose(frame='odom'|'map'|'gt')  # p[0] : X, p[1] : Y, p[2] : theta
v = getSpeed()      # v[0]: linear x, v[1]: angular z

# range distance

d = obstacleDistance(dir_deg=0)


# audio

sound(name)
say(text, language='en')
s = asr()


# modim

show_image(value, which='default')
show_text(value, which='default')


# vision

img = getImage()
n = faceDetection(img)
(label,conf) = mobilenetObjrecClient(img[,server,port])
b = tagTrigger()  # boolean
id = tagID()      # id
d = tagDistance() # [m]
a = tagAngle()    # [deg]


# utils

wait(sec)		    # Wait for X seconds
b = marrtinoOK()	# returns 'true' if the robot is ready
d = distance(p1,p2)	# Euclidean distance between points p1 and p2
display(x) 		    # Print the content of 'x' or the result of function 'x' in the Display area 


# simulator

stage_setpose(gx,gy,gth_deg)    # place the simulated robot in gx,gy,gth_deg
</listing>

<br>
<hr>
<br>

<h4>Android smartphone functions</h4>

<p>For exploiting your Android smartphone sensors, "ROS Android Sensors Driver" app is required. Please download and install it from Google Play Store.</p>

<a href="https://play.google.com/store/apps/details?id=org.ros.android.sensors_driver" target="_blank">Link to the page</a>

<p>or</p>

<p>Use this QR code</p>

<img src="QRAndroidDriver.png">

<p>Then, open the App and put the following text in the text area:</p>

<listing style="font-size:125%;">
http://[your_marrtino_ip]:11311
</listing>

<p>substituting "[your_marrtino_ip]" with the IP address of your MARRtino robot or your simulator.</p>




<br><br><br>

</div>


                <!-- ****** SCRIPTS ****** -->

<script src="../js/jquery-2.1.1.min.js"></script>
<script src="../js/materialize.js"></script>
<script src="../js/init.js"></script>

  <script>

    document.getElementById("run_btn").disabled = true;
    document.getElementById("stop_btn").disabled = true;

    function runCode() {
      var code = document.getElementById("code").value;
      wsrobot_send(code);
    }

    function stopCode() {
      // quit the program and stop the robot
      wsrobot_send("stop"); 
    }

    function check_connection() {
        console.log("check connection")
        if (wsrobot_connected()) {
            console.log("wsrobot_connected true")
            document.getElementById("connection").innerHTML = "<font color='green'>Connected</font>";
            document.getElementById("run_btn").disabled = false;
            document.getElementById("stop_btn").disabled = false;
        }
        else {
            console.log("wsrobot_connected false")
            document.getElementById("connection").innerHTML = "<font color='red'>Not Connected</font>";
            document.getElementById("run_btn").disabled = true;
            document.getElementById("stop_btn").disabled = true;
        }
    }

    function connect() {
        wsrobot_init(9913);  // init websocket robot
        setTimeout(check_connection, 1000);
    }

    function disconnect() {
        wsrobot_quit();  // init websocket robot
        setTimeout(check_connection, 1000);
    }


    window.setInterval(function()
    {
        document.getElementById('image').src = "../viewer/img/lastimage.jpg?random="+new Date().getTime();
    }, 5000);

  </script>

</body>
</html>

