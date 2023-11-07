<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <title>MARRtino Social Interface</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <script src="js/jquery-3.4.1.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="js/roslib.min.js"></script>
  <script type="text/javascript" src="js/eventemitter2.min.js"></script>
  <style>
  input[type=range][orient=vertical]
{
    writing-mode: bt-lr; /* IE */
    -webkit-appearance: slider-vertical; /* WebKit */
    width: 8px;
    height: 175px;
    padding: 0 5px;
}
</style>
  <script type="text/javascript" type="text/javascript">
    
    var ros = new ROSLIB.Ros({
 
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

   //* A topic for messaging.
var spalladxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/spalladx_controller/command',
  messageType: 'std_msgs/Float64'
});  

   //* A topic for messaging.
var spallasxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/spallasx_controller/command',
  messageType: 'std_msgs/Float64'
});  

   //* A topic for messaging.
var spalladxjTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/spalladxj_controller/command',
  messageType: 'std_msgs/Float64'
});  
//* A topic for messaging
var spallasxjTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/spallasxj_controller/command',
  messageType: 'std_msgs/Float64'
});  

//* A topic for messaging.
var sgomitodxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/gomitodx_controller/command',
  messageType: 'std_msgs/Float64'
});  

   //* A topic for messaging.
var gomitosxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/gomitosx_controller/command',
  messageType: 'std_msgs/Float64'
});  

   //* A topic for messaging.
var handdxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/handdx_controller/command',
  messageType: 'std_msgs/Float64'
});  

   //* A topic for messaging.
var handsxTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/handsx_controller/command',
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

function spalladx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 spalladxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("spalladx");   
}
function spallasx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 spallasxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("spallasx");   
}


function spalladxj( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 spalladxjTopic.publish(msg); // error here als
 console.log(msg);
 console.log("spalladxj");   
}
function spallasxj( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 spallasxjTopic.publish(msg); // error here als
 console.log(msg);
 console.log("spallasxj");   
}

function gomitodx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 gomitodxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("gomitodx");   
}
function gomitosx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 gomitosxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("gomitosx");   
}


function handdx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 handdxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("handdx");   
}
function handsx( value ){
var msg= new ROSLIB.Message({
      data: value     
 });
 handsxTopic.publish(msg); // error here als
 console.log(msg);
 console.log("handsx");   
}




   //* A topic for messaging.
var emotionTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/social/emotion',
  messageType: 'std_msgs/String'
});

   //* A topic for messaging.
   
var speechTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/speech/to_speak',
  messageType: 'std_msgs/String'
});


function speak( testo){
var msg_speak = new ROSLIB.Message({
      data: testo
 });
 FaceExpression('speak')
 speechTopic.publish(msg_speak); // error here als
 console.log(msg_speak);
 
 console.log("speech");   
}

function normal(){
var msg_happy = new ROSLIB.Message({
      data :  'happy'   
 });
 emotionTopic.publish(msg_happy); // error here als
 console.log("happy");   
}

function start_speak(){
var msg_speak = new ROSLIB.Message({
      data :  'speak'   
 });
 emotionTopic.publish(msg_speak); // error here als
 console.log("start speech");   
}


function FaceExpression( face){
  var mymsg = new ROSLIB.Message({
       data :  face   
  });
  emotionTopic.publish(mymsg); // error here als

  console.log(face);   
}




function normal(){
  var mymsg = new ROSLIB.Message({
       data :  'normal'   
  });
  emotionTopic.publish(mymsg); // error here als

  console.log("normal");   
}


function startBlinking(){
  var mymsg = new ROSLIB.Message({
       data :   'startblinking'   
  });
  emotionTopic.publish(mymsg); // error here als

  console.log("startblinking");   
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

    spalladxRange = document.getElementById("robot-spalladx");
    spalladxRange.oninput = function() {
        value = (((spalladxRange.value /100) -0.5 )*3 )+ 2.5;
		console.log(value);
		spalladx(value);
		 } 

    spallasxRange = document.getElementById("robot-spallasx");
    spallasxRange.oninput = function() {
        value = (((spallasxRange.value /100) -0.5)*3 )+ 2.5;
		console.log(value);
		spallasx(value);
		 } 
    spalladxjRange = document.getElementById("robot-spalladxj");
    spalladxjRange.oninput = function() {
        value = (((spalladxjRange.value /100) - 0.5)*3 )+ 2.5;
		console.log(value);
		spalladxj(value);
		 } 
     
    spallasxjRange = document.getElementById("robot-spallasxj");
    spallasxjRange.oninput = function() {
      value = (((spallasxjRange.value /100) -0.5)*3 )+ 2.5;
		console.log(value);
		spallasxj(value);
		 } 
  } 

     
    window.onload = function () {
	  
      
	  initPanTilt();
    }

  </script>j
 
  

</head>

<body>
  
<?php include "../social/nav.php" ?>


<div class="container-fluid">
  <div class="row">
    <div class="col-md-12"  style="background-color:yellow;" align="center" ><h2>EMOTIONS</h2></div>

  </div>
  <div class="row">
    <div class="col-md-12">. </div>

  </div>
  <div class="row">
    
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('normal')">Normal</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('angry')">angry</button></div>
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('happy')">Happy</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('sad')">sad</button></div>
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('surprise')">Surprise</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('sings')">sings</button></div>
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('startblinking')">Start Blinking</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('stopblinking')">Stop Blinking</button></div>
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('speak')">Speak</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('normal')">stop </button></div>
    <div class="col-md-1"></div>
    <div class="col-md-1"></div>
    <div class="col-md-1"></div>
    <div class="col-md-1" align="right"> <input type="range" orient="vertical"id="robot-tilt" /> </div>
	<div class="col- md-2">
	 
	  <div class="iframe-container"><iframe loading="lazy" src="/social/marrtina.html"></iframe></div>
	   <input  type="range" min="0" max="100" style="width:100%;" id="robot-pan" >
   </div>
   
  </div>
  <div class="row">
      <div class="col-md-6"></div>
	    <div class="col-md-1" align="right"> <input type="range" id="robot-spalladxj" /> </div>
      <div class="col-md-1"></div>
      <div class="col-md-1" align="right"> <input type="range" id="robot-spallasxj" /> </div>
	 </div>
  <div class="row">
      <div class="col-md-6"></div>
	    <div class="col-md-1" align="right"> <input type="range" orient="vertical" id="robot-spalladx" /> </div>
      <div class="col-md-1"></div>
      <div class="col-md-1" align="right"> <input type="range" orient="vertical" id="robot-spallasx" /> </div>
	 </div>

  </div>
  <!--
  <div class="row">
     <div class="col-md-12">
	 <input  type="range" min="15" max="80" style="width:80%;" id="robot-pan">
	 </div>
	 
 </div>
 -->
<!--
 
  <div class="row">
    <div class="col-md-12"  style="background-color: yellow;" align="center" ><h2>SPEAK</h2></div>

  </div>
  <div class="row">
    <div class="col-md-12">. </div>

  </div>
  <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto0" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto0').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto1" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto1').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto2" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto2').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto3" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto3').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto4" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto4').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto5" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto5').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto6" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto6').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto7" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto7').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto8" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto8').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
</div>
 <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto9" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto9').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto10" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto10').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
 </div>
 <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto11" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto11').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto12" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto12').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>
 </div>

 <div class="row">
    <div class="col-md-2">
       <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto13" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto13').value)" type="button" id="button-addon2">Speak</button>
      </div>
    </div>
    <div class="col-md-2">
      <div class="input-group mb-3">
        <input type="text" class="form-control" id="idtesto14" placeholder="Text" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto14').value)" type="button" id="button-addon2">Speak</button>
      </div>
   </div>

  -->
 </div>

    
</body>

</html>



