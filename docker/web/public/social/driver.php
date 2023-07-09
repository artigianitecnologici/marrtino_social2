<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8" />
  <title>MARRtino App Inventor Interface</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  
  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <script src="js/jquery-3.4.1.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="js/roslib.min.js"></script>
  <script type="text/javascript" src="js/eventemitter2.min.js"></script>
  <style>

</style>
  <script type="text/javascript" type="text/javascript">
    
    var ros = new ROSLIB.Ros({
 
      url: 'ws:' + window.location.hostname +':9090'
 
    });

    ros.on('connection', function () {
        console.log("Connected");
    });

    ros.on('error', function (error) {
        console.log("Error");
    });

    ros.on('close', function () {
        console.log("Closed");
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
   
var speechTopic = new ROSLIB.Topic({
  ros: ros,
  name : '/speech/to_speak',
  messageType: 'std_msgs/String'
});


function speak( testo){
var msg_speak = new ROSLIB.Message({
      data: testo
 });
 start_speak();
 speechTopic.publish(msg_speak); // error here als
 console.log(msg_speak);
 //normal();
 console.log("speech");   
}



function start_speak(){
var msg_speak = new ROSLIB.Message({
      data :  'speak'   
 });
 //emotionTopic.publish(msg_speak); // error here als
 console.log("start speech");   
}




     
    window.onload = function () {
	  
      
	  //initPanTilt();
    }

  </script>
 
  

</head>
<body>
  
<?
    $myfile = fopen("logs.txt", "a") or die("Unable to open file!");
   
    fwrite($myfile, "time");
    

    echo "Test";
    $key=trim($_POST['key']);
    $testo=trim($_POST['testo']);

    fwrite($myfile, $testo);


     
    echo "<script>speak('" . $testo ."')</script>";

    fclose($myfile);
    if($testo<>""&&$key<>"")
    {
        if($key=="keytest") echo "$testo";
    }
?>