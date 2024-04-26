<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Blockly Robot</title>
  <script src="blockly/blockly_compressed.js"></script>
  <script src="blockly/blocks_compressed.js"></script>
  <script src="blockly/javascript_compressed.js"></script>
  <script src="blockly/python_compressed.js"></script>
  <script src="blockly/msg/js/en.js"></script>
  <script src="robot_blocks.js"></script>
  <script src="robot_blocks_python.js"></script>
  <script src="websocket_robot.js"></script>
  

  <!-- Bootstrap CSS -->
  <link rel="stylesheet" href="bootstrap/css/bootstrap.min.css">
  <!--<script src="js/jquery-3.4.1.min.js"></script>-->
  <script src="bootstrap/js/bootstrap.min.js"></script>
  <style>
    body {
      background-color: #fff;
      font-family: Ubuntu, sans-serif;
    }
    h1 {
      font-weight: normal;
      font-size: 140%;
    }
  </style>
</head>
<body>


  <?php include "../social/nav.php" ?>

  <div class="container-fluid">


  </div>
    <div class="row">
       <div class="col-md-6">
        <!--<button class="btn btn-outline-success" id="hide_code" onclick="hide_blockly() ">Python</button>-->
        <button class="btn btn-outline-success" id="hide_code" onclick="show_blockly() ">Blockly</button>
        <button class="btn btn-outline-primary" onclick="showCode()">Show code</button>
        <button class="btn btn-outline-primary" id="run_btn" onclick="runCode()">Run</button>
        <button class="btn btn-outline-danger" id="stop_btn" onclick="stopCode()">Stop</button>
        <button class="btn btn-outline-warning" id="loadfile_btn" onclick="load_from_file()">Load file</button>
        <button class="btn btn-outline-success"  id="savefile_btn" onclick="save_to_file()">Save file</button>
        
        </div>
       <div class="col-md-6">
          Robot IP 
          <script>
           document.write("<td><input type=\"text\" name=\"IP\" id=\"IP\" value=\"" + 
                window.location.hostname + "\" width=240></td>")
        </script>
         <button onclick="connect()">Connect</button> 
          <button onclick="disconnect()">Disconnect</button> 
          <!--
          <div id="connection"><font color='red'>Not Connected</font> </div>
     
          Status 
          <div id="status" style="color: blue;" >Idle</div>  -->
      </div>

    </div>
    
    <div class="row">
       <div class="col-md-9">
           
           <div id="codeDiv" style="height: 480px; width: 100%; background-color: #DDDDDD; font-size: 120%;display: none;">Python Code</div>
           <div id="blocklyDiv" style="height: 480px; width: 100%;display: block;">Blockly workspace </div>

<xml xmlns="http://www.w3.org/1999/xhtml" id="toolbox" style="display: none;">

<category colour="120" name="Robot">

<block type="begin"></block>
<block type="end"></block>
<block type="forward">
  <value name="steps">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>
<block type="backward">
  <value name="steps">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>
<block type="left">
  <value name="steps">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>
<block type="right">
  <value name="steps">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>
<block type="turn">
  <value name="degrees">
    <block type="math_number">
      <field name="NUM">90</field>
    </block>
  </value>
</block>
<block type="wait">
  <value name="seconds">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>
<block type="setSpeed">
  <value name="tv">
    <block type="math_number">
      <field name="NUM">0.0</field>
    </block>
  </value>
  <value name="rv">
    <block type="math_number">
      <field name="NUM">0.0</field>
    </block>
  </value>
  <value name="time">
    <block type="math_number">
      <field name="NUM">0.1</field>
    </block>
  </value>
</block>

</category>

<category colour="0" name="Sensors">

<block type="obstacle_distance"></block>
<block type="get_pose"></block>

</category>
<category colour="120" name="Social">
<block type="gesture"> </block>
<block type="head_position"> </block>
<block type="status"> </block>
<block type="face"> </block>
<block type="right_shoulder_flexion"> </block>
<block type="left_shoulder_flexion"> </block>
<block type="right_shoulder_rotation"> </block>
<block type="left_shoulder_rotation"> </block>
<block type="right_elbow"> </block>
<block type="left_elbow"> </block>
<block type="hand_right"> </block>
<block type="hand_left"> </block>
<block type="pan"> </block>
<block type="tilt"> </block>

<block type="get_nro_of_face"></block>
</category>
<category colour="0" name="Code">
 <!-- 
<block type="wait_user_speaking">
  <value name="seconds">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block> -->

<block type="ask_chatgpt">
  <value name="text">
    <block type="text">
      <field name="TEXT">your question</field>
    </block>
  </value>
</block>
<block type="user_say"></block>
<block type="wait_user_say"></block>
<block type="clear-asr"></block>
<block type="run_python">

   <value name="text">
      <block type="text">
        <field name="TEXT">#your code here</field>
      </block>
      
  </value>
</block>

</category>
<category id="catLogic" name="Logic">
      <block type="controls_if"></block>
      <block type="logic_compare"></block>
      <block type="logic_operation"></block>
      <block type="logic_negate"></block>
      <block type="logic_boolean"></block>
      <block type="logic_null"></block>
      <block type="logic_ternary"></block>
    </category>

<category colour="50" name="Audio">

<block type="say">
  <value name="text">
    <block type="text">
      <field name="TEXT">hello</field>
    </block>
  </value>
  <value name="lang">
    <block type="text">
      <field name="TEXT">en</field>
    </block>
  </value>
</block>
<block type="sound">
  <value name="name">
    <block type="text">
      <field name="TEXT">bip</field>
    </block>
  </value>
</block>

</category>

<category colour="60" name="Vision">
   <block type="tag_trigger"></block>
   <block type="tag_id"></block>
   <block type="tag_distance"></block>
   <block type="tag_angle"></block>
   <block type="get_image"></block>
   <block type="face_detection"></block>
</category>

<category colour="200" name="Controls">

<block type="controls_if"></block>

<block type="controls_whileUntil"></block>

<block type="controls_repeat_ext">
  <value name="TIMES">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
</block>



</category>

<category colour="200" name="Op & Fn">

<block type="logic_compare"></block>

<block type="distance"></block>

<block type="marrtino_ok"></block>

<block type="random">
  <value name="min">
    <block type="math_number">
      <field name="NUM">1</field>
    </block>
  </value>
  <value name="max">
    <block type="math_number">
      <field name="NUM">90</field>
    </block>
  </value>
</block>

<block type="display">
  <value name="TEXT">
  </value>
</block>

<block type="math_number">
  <field name="NUM">1</field>
</block>

<block type="math_arithmetic"></block>

<block type="text">
  <field name="TEXT"></field>
</block>

</category>

<category name="Variables" colour="330" custom="VARIABLE"></category>
<category name="Functions" colour="290" custom="PROCEDURE"></category>

</xml>

<xml xmlns="http://www.w3.org/1999/xhtml" id="startBlocks" style="display:none">
<variables></variables>
<block type="begin" id="begin0" x="100" y="20"></block>
<block type="end" id="end0" x="100" y="140"></block>
</xml>
<!-- eof blockly -->


      </div>
      <div class="col-md-3">Face<div class="iframe-container"><iframe loading="lazy" src="/social/marrtina02.html"></iframe>
                            <div class="iframe-container"><iframe width="100%" height="250" loading="lazy" src="http://10.3.1.1:8080/social/onlyvideo.php"></iframe>
    
     </div>
         </div>
      
    </div>
  </div>



 
    
    
    
   

<br>

  <table border=0>
  <tr>  <th>Display</th>  </tr>
  <tr>
  <td style="color:#0000FF; background-color: #EEFFCC; font-size: 150%;" width=500 height=20>
    <div id="display">
    </div>    d
  </td>
  </tr>

 
                <!-- ****** SCRIPTS ****** -->

  <script>

    var demoWorkspace = Blockly.inject('blocklyDiv',
        // options
        {media: 'blockly/media/',
         toolbox: document.getElementById('toolbox'),
         scrollbars : true,
         grid : {
		        spacing : 20, 
		        length : 1, 
		        colour : '#888', 
		        snap : false
	        },
	    zoom : {
		    controls : true, 
		    wheel : true, 
		    startScale : 1.0, 
		    maxScale : 3, 
		    minScale : 0.25, 
		    scaleSpeed : 1.1
	      }
        });

    Blockly.Xml.domToWorkspace(document.getElementById('startBlocks'),
                               demoWorkspace);

    //document.getElementById("run_btn").disabled = true;
    //document.getElementById("stop_btn").disabled = true;


    function showCode() {
      // Generate Python code and display it.
      hide_blockly();
      Blockly.Python.INFINITE_LOOP_TRAP = null;
      var code = Blockly.Python.workspaceToCode(demoWorkspace);
      //alert(code);
      document.getElementById("codeDiv").innerHTML = "<pre>"+code+"</pre>";
    }

    function runCode() {
      // Generate JavaScript code and run it.
      window.LoopTrap = 1000;
      //Blockly.Python.INFINITE_LOOP_TRAP =
      //    'if (--window.LoopTrap == 0) throw "Infinite loop.";\n';
      Blockly.Python.INFINITE_LOOP_TRAP = null;
      var code = Blockly.Python.workspaceToCode(demoWorkspace);
      document.getElementById("codeDiv").innerHTML = "<pre>"+code+"</pre>";
      wsrobot_send(code);
    }

    function stopCode() {
      // quit the program and stop the robot
      wsrobot_send("stop"); 
    }

    function saveCode() {
        var xml = Blockly.Xml.workspaceToDom(demoWorkspace);
        var xml_text = Blockly.Xml.domToText(xml); 
        //console.log('save block code')
        //console.log(xml_text)
        document.getElementById("xmlSave").innerText = xml_text;
    }

    function loadCode() {
        var xml_text = document.getElementById("xmlLoad").value;
        var xml = Blockly.Xml.textToDom(xml_text);
        demoWorkspace.clear()
        Blockly.Xml.domToWorkspace(xml, demoWorkspace);
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
        wsrobot_init(9913);  // init websocket robot old 9930
        setTimeout(check_connection, 1000);
    }

    function disconnect() {
        wsrobot_quit();  // init websocket robot
        setTimeout(check_connection, 1000);
    }
    

    function load_from_file() {
      var can_load_file = false;
      //if (demoworkspace.getAllBlocks().length > 0) {
        can_load_file = confirm("Current workspace is not empty. Do you want to override it?");
      //} else {
      //  can_load_file = true;
      //}

      if (true == can_load_file) {
        var input_field_name = 'load_workspace_from_file_input';
        var file_input = document.getElementById(input_field_name);
        if (null == file_input) {
            file_input = document.createElement('input');
            file_input.type = 'file';
            file_input.id = input_field_name;
            file_input.name = input_field_name;
            file_input.addEventListener('change',
                      function (evt) {
                          var files = evt.target.files;
                          if (files.length > 0) {
                              var file = files[0];
                              var reader = new FileReader();
                              reader.onload = function () {
                                  demoWorkspace.clear();
                              
                                  var xml = Blockly.Xml.textToDom(this.result);
                                  console.log("Loading workspace from file.");
                                  Blockly.Xml.domToWorkspace(demoWorkspace, xml);
                              };
                              reader.readAsText(file);
                              // This is done in order to allow open the same file several times in the row
                              document.body.removeChild(file_input);
                          }
                      }, false);
            // Hidding element from view
            file_input.style = 'position: fixed; top: -100em';
        document.body.appendChild(file_input);
        }
        file_input.click();
      }
    }

    function save_to_file() {
      var filename = 'blockly_workspace.xml';
      var xml = Blockly.Xml.workspaceToDom(demoWorkspace);
      var xml_text = Blockly.Xml.domToText(xml); 

      var blob = new Blob([xml_text], {type: 'text/xml'});
      if (window.navigator.msSaveOrOpenBlob) {
          window.navigator.msSaveBlob(blob, filename);
      } else {
          var elem = window.document.createElement('a');
          elem.href = window.URL.createObjectURL(blob);
          elem.download = filename;
          document.body.appendChild(elem);
          elem.click();
          document.body.removeChild(elem);
      }
      console.log("Workspace saved.");
    }


    function hide_blockly() {
      document.getElementById("blocklyDiv").style.display = 'none';
      document.getElementById("codeDiv").style.display = 'block';
      //window.location.reload(true);
    }

    function show_blockly() {
      document.getElementById("blocklyDiv").style.display = 'block';
      document.getElementById("codeDiv").style.display = 'none';
      //window.location.reload(true);
      // alert("resizing");
      // window.dispatchEvent(new Event('resize'));
  };


  </script>

</body>
</html>
