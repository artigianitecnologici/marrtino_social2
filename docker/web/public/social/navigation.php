<!DOCTYPE html>
<html>

<head>


  <meta charset="utf-8" />
  <title>TeleMARR</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <script src="js/jquery-3.4.1.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="js/roslib.min.js"></script>
  <script type="text/javascript" src="js/nipplejs.js"></script>
  <script type="text/javascript" src="js/eventemitter2.min.js"></script>
  <script type="text/javascript" src="js/keyboardteleop.min.js"></script>
  <script type="text/javascript" type="text/javascript">
    var teleop;
    var ros = new ROSLIB.Ros({
      //url: 'wss:ufficioeffegi.homepc.it:9090'
	 url: 'ws:' + window.location.hostname +':9090'
    });

    ros.on('connection', function () {
      document.getElementById("status").innerHTML = "Connected";
    });

    ros.on('error', function (error) {
      document.getElementById("status").innerHTML = "Error";
    });

    ros.on('close', function () {
      document.getElementById("status").innerHTML = "Closed";
    });
    // 
    var txt_listener = new ROSLIB.Topic({
      ros: ros,
      name: '/txt_msg',
      messageType: 'std_msgs/String'
    });

    txt_listener.subscribe(function (m) {
      document.getElementById("msg").innerHTML = m.data;
      
    });
	// SONAR
	var sonar0_listener = new ROSLIB.Topic({
      ros: ros,
      name: '/sonar_0/range',
      messageType: 'sensor_msgs/Range'
    });

    sonar0_listener.subscribe(function (m) {
      document.getElementById("sonar0").innerHTML = m.data;
      
    });

    cmd_vel_listener = new ROSLIB.Topic({
      ros: ros,
      name: "/cmd_vel",
      messageType: 'geometry_msgs/Twist'
    });

	initTeleopKeyboard = function() {
    // Use w, s, a, d keys to drive your robot

    // Check if keyboard controller was aready created
    if (teleop == null) {
        // Initialize the teleop.
        teleop = new KEYBOARDTELEOP.Teleop({
            ros: ros,
            topic: '/cmd_vel'
        });
    }

    // Add event listener for slider moves
    robotSpeedRange = document.getElementById("robot-speed");
    robotSpeedRange.oninput = function () {
        teleop.scale = robotSpeedRange.value / 100
    }
}
    move = function (linear, angular) {
      var twist = new ROSLIB.Message({
        linear: {
          x: linear,
          y: 0,
          z: 0
        },
        angular: {
          x: 0,
          y: 0,
          z: angular
        }
      });
      cmd_vel_listener.publish(twist);
    }

    createJoystick = function () {
      var options = {
        zone: document.getElementById('zone_joystick'),
        threshold: 0.1,
        position: {left: '80%', top: '65%'},
        mode: 'static',
        size: 250,
        color: 'red',
      };
      manager = nipplejs.create(options);

      linear_speed = 0;
      angular_speed = 0;

      manager.on('start', function (event, nipple) {
        timer = setInterval(function () {
          move(linear_speed, angular_speed);
        }, 25);
      });

      manager.on('move', function (event, nipple) {
        max_linear = 0.2; // m/s
        max_angular = 1.0; // rad/s
        max_distance = 75.0; // pixels;
        linear_speed = Math.sin(nipple.angle.radian) * max_linear * nipple.distance/max_distance;
	    angular_speed = -Math.cos(nipple.angle.radian) * max_angular * nipple.distance/max_distance;
      });

      manager.on('end', function () {
        if (timer) {
          clearInterval(timer);
        }
        self.move(0, 0);
      });
    }

//* A topic for messaging.
var panTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/pan_controller/command',
  messageType: 'std_msgs/Float64'
});  

var tiltTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/tilt_controller/command',
  messageType: 'std_msgs/Float64'
});  

function pan( value ){
var msg_pan = new ROSLIB.Message({
      data: value     
 });
 panTopic.publish(msg_pan); // error here als
 console.log(msg_pan);
 console.log("pan");   
}



function tilt( value ){
var msg_tilt = new ROSLIB.Message({
      data: value     
 });
 tiltTopic.publish(msg_tilt); // error here als
 console.log(msg_tilt);
 console.log("tilt");   
}
	
  initPanTilt= function() {
   // Add event listener for slider moves
    headPanRange = document.getElementById("robot-pan");
    headPanRange.oninput = function() {
        value = ((headPanRange.value /100) - 0.5)*2;
		console.log(value);
		pan(value);
		
		
    } 
	headTiltRange = document.getElementById("robot-tilt");
    headTiltRange.oninput = function() {
        value = ((headTiltRange.value /100) -0.5) * -1;
		console.log(value);
		tilt(value);
		
		
    } 
  } 
    window.onload = function () {
      initPanTilt();
      video = document.getElementById('video');
	   // Populate video source 
         
          video.src = 'http://' + window.location.hostname +':29090/stream?topic=/rgb/image_raw&type=mjpeg&quality=100';

	  //video.src = "http://192.168.1.119:29090/stream?topic=/usb_cam/image_raw&type=mjpeg&quality=100";
	  video.onload = function () {
			createJoystick();
			initTeleopKeyboard();
        }	
	  
    }

  </script>
  
<style>

div.joy {
   position: absolute;
   bottom: 10px;
   right: 16px;
  
}
.container {
  position: relative;
}
.bottomright {
  position: absolute;
  bottom: 8px;
  right: 16px;
  font-size: 18px;
}

img { 
  width: 100%;
  height: auto;
  opacity: 1;
}
</style>
</head>

<body>
<?php include "nav.php" ?>

 

<div class="container-fluid">
  <div class="row">
    <div class="col-md-2" align="right"> <input type="range" orient="vertical"id="robot-tilt" /> </div>
    <div class="col-md-8">
	    <img style="width:640;height:480;" src=""  alt="" id="video" />
      

	    <div id="zone_joystick" style="joy"></div>
    </div>
</div>
  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-1">

      <label for="robot-speed">  <strong>Pan</strong> </label>
    </div>
    <div class="col-md-7">
	    <input  type="range" min="0" max="100" style="width:80%;" id="robot-pan" >
    </div>
     
        
    </div>
    <div class="col-md-2"></div>
  </div>
  <div class="row">
    <div class="col-md-2"></div>
    <div class="col-md-1">

    <label for="robot-speed">  <strong>Robot speed</strong> </label>
    </div>
    <div class="col-md-7">
    <input  type="range" min="15" max="80" style="width:80%;" id="robot-speed">
    </div>
       
   	 
        
    </div>
    <div class="col-md-2"></div>
  </div>

</div>
 <!--
	<p>txt_msg: <span id="msg"></span></p>
	<p>Sonar <span id="sonar0"></span></p>
   <h1>Simple ROS User Interface</h1>
  <p>Connection status: <span id="status"></span></p>
  <p>Sonar on /txt_msg: <span id="msg"></span></p>
 -->
  


</body>

</html>



