<?php 

if ( !empty($_POST)) {
   // print_r($_POST);
   $flda= $_POST['idtesto'] . "\n";
   $fld0= $_POST['idtesto0'] . "\n";
   $fld1= $_POST['idtesto1'] . "\n";
   $fld2= $_POST['idtesto2'] . "\n";
   $fld3= $_POST['idtesto3'] . "\n";
   $fld4= $_POST['idtesto4'] . "\n";
   $fld5= $_POST['idtesto5'] . "\n";
   $fld6= $_POST['idtesto6'] . "\n";
   $fld7= $_POST['idtesto7'] . "\n";
   $fld8= $_POST['idtesto8'] . "\n";
   $fld9= $_POST['idtesto9'] . "\n";
   $fld10= $_POST['idtesto10'] . "\n";
   $fld11= $_POST['idtesto11'] . "\n";
   $fld12= $_POST['idtesto12'] . "\n";
   $fld13= $_POST['idtesto13'] . "\n";
   $fld14= $_POST['idtesto14'] . "\n";
   $myfile = fopen('tmp/facerobot.txt', 'w')  or die("Unable to open file!");
   fwrite($myfile,  $flda);
   fwrite($myfile,  $fld0); 
   fwrite($myfile,  $fld1);
   fwrite($myfile,  $fld2);  
   fwrite($myfile,  $fld3);  
   fwrite($myfile,  $fld4);
   fwrite($myfile,  $fld5);  
   fwrite($myfile,  $fld6);
   fwrite($myfile,  $fld7);
   fwrite($myfile,  $fld8);
   fwrite($myfile,  $fld9);  
   fwrite($myfile,  $fld10);
   fwrite($myfile,  $fld11);  
   fwrite($myfile,  $fld12);
   fwrite($myfile,  $fld13);
   fwrite($myfile,  $fld14);
   fclose($myfile);

  } else {
    $myfile = fopen('tmp/facerobot.txt', 'r');
    $flda = fgets($myfile);
    $fld0= fgets($myfile);
    $fld1= fgets($myfile);
    $fld2= fgets($myfile);
    $fld3= fgets($myfile);
    $fld4= fgets($myfile);
    $fld5= fgets($myfile);
    $fld6= fgets($myfile);
    $fld7= fgets($myfile);
    $fld8= fgets($myfile);
    $fld9= fgets($myfile);
    $fld10= fgets($myfile);
    $fld11= fgets($myfile);
    $fld12= fgets($myfile);
    $fld13= fgets($myfile);
    $fld14= fgets($myfile);
    fclose($myfile);

  } 


?>


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

var gestureTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/social/gesture',
  messageType: 'std_msgs/String'
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
  startgesture()
  speechTopic.publish(msg_speak); // error here als
  console.log(msg_speak);
  
  console.log("speech");   
}


function speaken( testo){
testo=testo+'###en';  
var msg_speak = new ROSLIB.Message({
      data: testo
 });
 FaceExpression('speak')
  startgesture()
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

function startgesture(){
  var mymsg = new ROSLIB.Message({
       data :  'gesture'   
  });
  gestureTopic.publish(mymsg); // error here als
  console.log("gesture");   
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
  } 

     
    window.onload = function () {
	    initPanTilt();
      video = document.getElementById('video');
      video.src = 'http://' + window.location.hostname +':29090/stream?topic=/rgb/image_raw&type=mjpeg&quality=100&width=256&height=192';
    }

  </script>
 
  

</head>

<body>


<?php include "../social/nav.php" ?>


<form action="facerobot.php" method="post">

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
    <div class="col-md-2"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('startblinking')">Start Blinking</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('stopblinking')">Stop Blinking</button></div>
    <div class="col-md-1"><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('speak')">Speak</button><br><button class="btn btn-outline-danger btn-lg" onclick="FaceExpression('normal')">stop </button></div>
    <div class="col-md-1"> <input class="btn btn-outline-success btn-lg" type="submit" name="submit" value="Salva"></div>
    <div class="col-md-1"></div>
    <div class="col-md-1" align="right"> <input type="range" orient="vertical"id="robot-tilt" /> </div>
	<div class="col-md-2">
	 

    <img  src=""  alt="" id="video" />
   <!--   <iframe loading="lazy" src="/social/marrtina02.html"></iframe>-->
	   <input  type="range" min="0" max="100" style="width:100%;" id="robot-pan" >
   </div>
   
  </div>
  <!--
  <div class="row">
     <div class="col-md-12">
	 <input  type="range" min="15" max="80" style="width:80%;" id="robot-pan">
	 </div>
	 
 </div>
 -->

 
  <div class="row">
    <div class="col-md-12"  style="background-color: yellow;" align="center" ><h2>SPEAK</h2></div>

  </div>
  <div class="row">
    <div class="col-md-12">. </div>

  </div>
  <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control" name="idtesto" id="idtesto" placeholder="Text" value="<?php echo $flda; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto0" id="idtesto0" placeholder="Text"  value="<?php echo $fld0; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto0').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto0').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto1"  id="idtesto1" placeholder="Text"  value="<?php echo $fld1; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto1').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto1').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto2" id="idtesto2" placeholder="Text"  value="<?php echo $fld2; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto2').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto2').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto3"  id="idtesto3" placeholder="Text"  value="<?php echo $fld3; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto3').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto3').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto4" id="idtesto4" placeholder="Text"  value="<?php echo $fld4; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto4').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto4').value)" type="button" id="button-addon2">EN</button>
      </div> 
   </div>
   </div>
   <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto5" id="idtesto5" placeholder="Text"  value="<?php echo $fld5; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto5').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto5').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto6"  id="idtesto6" placeholder="Text"  value="<?php echo $fld6; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto6').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto6').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
   </div>
   <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto7" id="idtesto7" placeholder="Text"  value="<?php echo $fld7; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto7').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto7').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto8" id="idtesto8" placeholder="Text"  value="<?php echo $fld8; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto8').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto8').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
</div>
 <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto9"  id="idtesto9" placeholder="Text"  value="<?php echo $fld9; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto9').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto9').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto10" id="idtesto10" placeholder="Text"  value="<?php echo $fld10; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto10').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto10').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
 </div>
 <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto11" id="idtesto11" placeholder="Text"  value="<?php echo $fld11; ?>" aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto11').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto11').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto12" id="idtesto12" placeholder="Text" value="<?php echo $fld12; ?>"  aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto12').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto12').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
 </div>

 <div class="row">
    <div class="col-md-6">
       <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto13"  id="idtesto13" placeholder="Text" value="<?php echo $fld13; ?>"  aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto13').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto13').value)" type="button" id="button-addon2">EN</button>
      </div>
    </div>
    <div class="col-md-6">
      <div class="input-group mb-3">
        <input type="text" class="form-control"  name="idtesto14"  id="idtesto14" placeholder="Text" value="<?php echo $fld14; ?>"  aria-label="Testo" aria-describedby="button-addon2">
        <button class="btn btn-outline-secondary" onclick="speak(document.getElementById('idtesto14').value)" type="button" id="button-addon2">IT</button>
        <button class="btn btn-outline-secondary" onclick="speaken(document.getElementById('idtesto14').value)" type="button" id="button-addon2">EN</button>
      </div>
   </div>
 </div>

  </form>
    
</body>

</html>



