<!-- * -->
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1.0"/>
  <title>SOCIAL CONFIGURATION v.2.0</title>
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <script src="js/jquery-3.4.1.min.js"></script>
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <!-- CSS  
  <link href="css/materialize.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  <link href="css/style.css" type="text/css" rel="stylesheet" media="screen,projection"/>
  -->
  <script src="js/websocket_robot.js"></script>
 

 

</head>

<body>

<!-- Nav Bar -->
<?php include "../social/nav.php" ?>
<!-- Eof Nav Bar -->

<div class="container-fluid">
  <div class="row">
 
    <div class="col-md-12"  style="background-color:yellow;" align="center" ><h2>MARRTINO SOCIAL CONFIGURATION</h2></div>

  </div>
  <div class="row">
  <div class="col-md-1"></div>
    <div class="col-md-4">
    IP:
    <script>
      document.write("<td><input type=\"text\" name=\"IP\" id=\"IP\" value=\"" + 
            window.location.hostname + "\" width=240>")
    </script>
    <button onclick="connect()" class="btn btn-primary btn-sm my-2 my-sm-0" type="submit">Connect</button>
  	<button onclick="disconnect()" class="btn btn-light btn-sm" style="margin-right:10px">Disconnect</button>
    </div>
    <div class="col-md-4">
    <div id="connection"><font color='red'>Not Connected</font></div>
    <!-- /
    <div id="status" style="color: blue;" >Idle</div>
   <p class="text-white">Connection status: <span id="status"></span></p>-->
     </div>
  </div>

  
</div>



<div class="row">
	<div class="col-md-1"></div>
    <div class="col-md-10">
    <table>
        <tr height=40>
        <td width=150><div id="ros" style="color: grey;" >ROS</div></td>
        <td width=150><div id="robot" style="color: grey;" >MARRtino</div></td>
  <!--  <td width=150><div id="turtle" style="color: grey;" >Turtlebot</div></td>
    <td width=150><div id="simrobot" style="color: grey;" >Simrobot</div></td> -->
  </tr>
  <!--
  <tr height=40>
    <td><span id="odom" style="color: grey;">odom</span>     
        <span id="odom_status" style="color: grey;">OFF</span>   </td>
    <td><span id="laser" style="color: grey;">laser</span>   
        <span id="laser_status" style="color: grey;">OFF</span> </td>
    <td><span id="sonar" style="color: grey;">sonar</span>
        <span id="sonar_status" style="color: grey;">OFF</span>   </td>
  </tr>
  <tr height=40>
    <td><span id="rgb" style="color: grey;">RGB</span>
        <span id="rgb_status" style="color: grey;">OFF</span>        </td>
    <td><span id="depth" style="color: grey;">Depth</span>
        <span id="depth_status" style="color: grey;">OFF</span>      </td>
  </tr>
-->
</table>

<!--
<table>
  <tr><td>TF</td></tr>
  <tr><td><div id="tf_map_odom" style="color: grey;">map -&gt; odom</div></td></tr>
  <tr><td><div id="tf_odom_base" style="color: grey;">odom -&gt; base_frame</div></td></tr>

  <tr><td><div id="tf_base_laser" style="color: grey;">base_frame -&gt; laser_frame</div></td></tr>
  <tr><td><div id="tf_base_rgb" style="color: grey;">base_frame -&gt; rgb_camera_frame</div></td></tr>
  <tr><td><div id="tf_base_depth" style="color: grey;">base_frame -&gt; depth_camera_frame</div></td></tr>
</table>

<p>-->
<button onclick="send_cmd('check')" class="btn waves-effect waves-light blue" style="margin-right:10px">Check status</button>
<button onclick="send_cmd('ros_quit')" class="btn waves-effect waves-light blue" style="margin-right:10px">Quit all</button>
<button id="shutdown_btn" onclick="send_cmd('shutdown')" class="btn waves-effect waves-light blue">Shutdown</button>
</p>
</div>
</div>




<div class="row">
<div class="col-md-1"></div>
<div class="col-md-5">

   Update Marrtino Social ( refresh page after update)

</div>




  <div class="row">
  <div class="col">
      <button id="social_update" onclick="send_cmd('updatesocialapps')" class="btn btn-outline-success btn-lg">Marrtino Social Update</button>  
   </div>
   <!--
    <div class="col">
      <button id="social_stop" onclick="send_cmd('shutdown')" class="btn btn-outline-success btn-lg">Shutdown </button>  
   </div>
   <div class="col">
    <button id="social_reset" onclick="send_cmd('social_reset')" class="btn btn-outline-danger btn-lg">Social Reset </button>  
   </div>
-->
  </div>

 
   
  
 </div>


<table class="table table-striped">
  <thead>
    <tr>
      <th scope="col">Release</th>
      <th scope="col">Software</th>
      <th scope="col">Description</th>
      <th scope="col">Type</th>
     
    </tr>
  </thead>
  <tbody>
    <?php
     $filename = 'release.csv';

     $handler = fopen($filename, 'r');
     
     while($data = fgetcsv($handler)) {
         $mydata = implode('', $data);
         $release =explode(";",$mydata);
         ?>
  
        <tr>
          <th scope="row"><?php echo $release[0];?></th>
          <td><?php echo $release[1];?></td>
         <td><?php echo $release[2];?></td>
          <td><?php echo $release[3];?></td>
        </tr>
         <?php

         #print_r($release);
     }
     
    fclose($handler);
    ?>
  
  </tbody>
</table>


 


<!-- The Modal -->
<div id="waitModal" class="modal">

  <!-- Modal content -->
  <div class="modal-content">
    <h2 align='center'>Please wait..</h2>
  </div>

</div>

</div>

</body>


<!-- ****** SCRIPTS ****** -->
<!--
<script src="js/jquery-2.1.1.min.js"></script>
<script src="js/materialize.js"></script>
<script src="js/init.js"></script>
-->
<script>


    function waitwindow_on() {
        var modal = document.getElementById('waitModal');
        modal.style.display = "block";
        console.log("waitwindow_on")
    }

    function waitwindow_off() {
        var modal = document.getElementById('waitModal');
        modal.style.display = "none";
        console.log("waitwindow_off")
    }

    // setTimeout(waitwindow_on(), 4000);
    

    //document.getElementById("simrobot_start_btn").disabled = false;


    // messages received from wsserver
    eventproc = function(event){
      v = event.data.split(' ');

      if (v[0]=='STATUS') {
          vs = '';
          for (i=1; i<v.length ; i++)
             vs += v[i]+' '
          vs = vs.trim();
          document.getElementById("status").innerHTML = vs;
          var d = new Date();
          console.log(d+" - status ["+vs+"]");
          if (vs=="Idle")
            waitwindow_off();
          else
            waitwindow_on();
      }
      else if (v[0]=='RESULT') {
          cv = v[2];
          console.log("log: "+ v[1] + " " + v[2])
          if (v[2]=='True' || parseFloat(v[2])>0) {
            //cv = "<font color='green'>"+v[2]+"</font>"
            d = document.getElementById(v[1])
            if (d!=null)
                d.style.color = 'green';
            //document.getElementById(v[1]+"_btn").style.color = 'green';

            //document.getElementById(v[1]+"_start_btn").disabled = false;
            //document.getElementById(v[1]+"_quit_btn").disabled = false;

            vst = v[1]+"_status"; // status label
            d = document.getElementById(vst);
            if (d!=null) {
                if (v[2]=='True')
                    d.innerHTML = 'OK';
                else
                    d.innerHTML = v[2];
                d.style.color = 'green';
            }



          }
          else if (v[2]=='False' || parseFloat(v[2])==0.0) {
            //cv = "<font color='red'>"+v[2]+"</font>"
            d = document.getElementById(v[1]);
            if (d!=null)
                d.style.color = 'red'
            //document.getElementById(v[1]+"_start_btn").disabled = false;
            //document.getElementById(v[1]+"_quit_btn").disabled = false;

            vst = v[1]+"_status"; // status label
            d = document.getElementById(vst);
            if (d!=null) {
                d.innerHTML = 'OFF';
                d.style.color = 'red';
            }
          }


      }
      else if (v[0]=='VALUE') {
          vs = '';
          for (i=2; i<v.length ; i++)
             vs += v[i]+' '
          document.getElementById(v[1]).innerHTML = vs;
      }
    }

    function connect() {
        wsrobot_init(9912);  // init websocket robot
        setTimeout(check_connection, 1000);
        websocket.onmessage = eventproc;
    }

    function disconnect() {
        wsrobot_quit();  // init websocket robot
        setTimeout(check_connection, 1000);
    }

    function check_connection() {
        console.log("check connection")
        if (wsrobot_connected()) {
            console.log("wsrobot_connected true")
            document.getElementById("connection").innerHTML = "<font color='green'>Connected</font>";
            //document.getElementById("run_btn").disabled = false;
            //document.getElementById("stop_btn").disabled = false;
        }
        else {
            console.log("wsrobot_connected false")
            document.getElementById("connection").innerHTML = "<font color='red'>Not Connected</font>";
            //document.getElementById("run_btn").disabled = true;
            //document.getElementById("stop_btn").disabled = true;
        }
    }

    function send_cmd(action) {
        wsrobot_send(action);
    }

 


</script>

</html>

