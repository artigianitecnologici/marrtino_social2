// User defined blocks

Blockly.Blocks['begin'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("begin");
    this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("begin of program");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['end'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("end");
    this.setPreviousStatement(true, null);
    this.setColour(0);
 this.setTooltip("end of program");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['forward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/up.png", 20, 20, "Forward"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("forward");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot moves forward");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['backward'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/down.png", 20, 20, "Backward"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("backward");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot moves backward");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/rotleft.png", 20, 20, "Left"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("left");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot turns left");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/rotright.png", 20, 20, "Right"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("right");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot turns right");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['wait'] = {
  init: function() {
    /*this.appendDummyInput().appendField(new Blockly.FieldImage("img/rotright.png", 20, 20, "Wait"));*/
    this.appendValueInput("seconds")
        .setCheck("Number")
        .appendField("wait");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot waits [seconds]");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['turn'] = {
  init: function() {
    /*this.appendDummyInput().appendField(new Blockly.FieldImage("img/rotright.png", 20, 20, "Turn"));*/
    this.appendValueInput("degrees")
        .setCheck("Number")
        .appendField("turn");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot turns [angle in degrees]");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['setSpeed'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("setSpeed");
    this.appendValueInput("tv")
        .setCheck("Number")
        .appendField("tv");
    this.appendValueInput("rv")
        .setCheck("Number")
        .appendField("rv");
    this.appendValueInput("time")
        .setCheck("Number")
        .appendField("time");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("robot speed tv [m/s], rv [rad/s] for time seconds");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['get_pose'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get_pose()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns the pose of the robot [x,y,theta]");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['random'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("random");
    this.appendValueInput("min")
        .setCheck("Number");
    this.appendValueInput("max")
        .setCheck("Number");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns a random number between min and max");
 this.setHelpUrl("");
  }
};



Blockly.Blocks['obstacle_distance'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("obstacle_distance")
        .appendField(new Blockly.FieldDropdown([["front","OPTIONFRONT"], ["left","OPTIONLEFT"], ["right","OPTIONRIGHT"], ["back","OPTIONBACK"]]), "direction");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns distance from obstable front|left|right");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['distance'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("distance");
    this.appendValueInput("P1")
        .setCheck(null);
    this.appendValueInput("P2")
        .setCheck(null);
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns distance between two poses");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['marrtino_ok'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("marrtino_ok");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns True if MARRtino is correctly running");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['display'] = {
  init: function() {
    this.appendValueInput("text").appendField("display");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(150);
 this.setTooltip("displays the argument on the web interface");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['say'] = {
  init: function() {
    this.appendDummyInput().appendField("say");
    this.appendValueInput("text");
    this.appendValueInput("lang").appendField("language");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(50);
 this.setTooltip("says the argument through audio server. languages: en, it, fr, de, es");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['sound'] = {
  init: function() {
    this.appendDummyInput().appendField("sound");
    this.appendValueInput("name");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(50);
 this.setTooltip("plays the sound through audio server");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['status'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Face Status")

        .appendField(new Blockly.FieldDropdown([["blink eye","startblinking"],["speech","speak"], ["stop speech","normal"] ]), "STATUS");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['face'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("Emotion")
        .appendField(new Blockly.FieldDropdown([["normal","normal"],["happy","happy"], ["sad","sad"],["sings","sings"],["surprise","surprise"], ["angry","angry"]]), "EMOTION");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['gesture'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("gesture")
        .appendField(new Blockly.FieldDropdown([["init","init"],["zero","zero"],["hello","hello"], ["left","left"],["right","right"]]), "ROBOT_GESTURE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Gesture");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['head_position'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("head_position")
        .appendField(new Blockly.FieldDropdown([["front","front"],["up","up"],["down","down"], ["left","left"],["right","right"]]), "HEAD_POSITION");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("Move head position");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['get_stt'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get_stt()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns speeh to text");
 this.setHelpUrl("");
  }
};
Blockly.Blocks['get_nro_of_face'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("get_nro_of_face()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns nro of face");
 this.setHelpUrl("");
  }
};
// Social
Blockly.Blocks['pan'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/pan.png", 20, 20, "Head pan"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("pan");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("head pan position");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['tilt'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "Head tilt"));
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("tilt");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("head tilt position");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['right_shoulder_flexion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "right_shoulder_flexion %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("right_shoulder_flexion");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("right_shoulder_flexion");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['left_shoulder_flexion'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "left_shoulder_flexion %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("left_shoulder_flexion");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("left_shoulder_flexion");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['right_shoulder_rotation'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "right_shoulder_rotation %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("right_shoulder_rotation");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("right_shoulder_rotation");
 this.setHelpUrl("");
  }
};



Blockly.Blocks['left_shoulder_rotation'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "left_shoulder_rotation %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("left_shoulder_rotation");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("left_shoulder_rotation");
 this.setHelpUrl("");
  }
};
Blockly.Blocks['right_elbow'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "right_elbow %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("right_elbow");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("right_elbow");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['left_elbow'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "left_elbow %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("left_elbow");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("left_elbow");
 this.setHelpUrl("");
  }
};
Blockly.Blocks['hand_right'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "Hand right %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("hand_right");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Hand Rotation");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['hand_left'] = {
  init: function() {
    this.appendDummyInput()
        .appendField(new Blockly.FieldImage("img/tilt.png", 20, 20, "hand_left SX %"));
    this.appendDummyInput()
        .appendField("sign")
        .appendField(new Blockly.FieldDropdown([["+","+"],["-","-"]]), "Sign");
    this.appendValueInput("steps")
        .setCheck("Number")
        .appendField("hand_left");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(120);
 this.setTooltip("Hand Left Rotation");
 this.setHelpUrl("");
  }
};


/**
 * Common HSV hue for all blocks in this category.

 Blockly.Blocks.variables.HUE = 160;

 Blockly.Blocks['run_python'] = {
   init: function() {
     this.appendDummyInput()
         .appendField("Run code")
         .appendField(new Blockly.FieldTextInput("#Enter your own python code"), "CODE_TEXT");
     this.setInputsInline(true);
     this.setPreviousStatement(true);
     this.setNextStatement(true);
     this.setColour(160);
     this.setTooltip('');
     this.setHelpUrl('http://robotics.surfweb.eu');
   }
 };
 */
 Blockly.Blocks['run_python'] = {
  init: function() {
    this.appendDummyInput().appendField("run_python");
    this.appendValueInput("text");
    this.setInputsInline(true);
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(0);
    this.setHelpUrl('http://robotics.surfweb.eu');
 this.setHelpUrl("");
  }
};

Blockly.Blocks['wait_user_say'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("wait_user_say()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns the user say - wait 10 sec");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['user_say'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("user_say()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns the user say");
 this.setHelpUrl("");
  }
};



Blockly.Blocks['clear-asr'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("clear-asr")
     //   .appendField(new Blockly.FieldDropdown([["clear","inclearit"],["zero","zero"],["hello","hello"], ["left","left"],["right","right"]]), "ROBOT_GESTURE");
    this.setPreviousStatement(true, null);
    this.setNextStatement(true, null);
    this.setColour(230);
 this.setTooltip("clear-asr");
 this.setHelpUrl("");
  }
};




Blockly.Blocks['ask_chatgpt'] = {
  init: function() {
    this.appendDummyInput().appendField("ask_chatgpt");
    this.appendValueInput("text");
    this.setInputsInline(true);
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("type ask to chatgpt");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['tag_trigger'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("tag_trigger()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns tag trigger (boolean)");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['tag_id'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("tag_id()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns tag ID");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['tag_distance'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("tag_distance()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns tag distance (m)");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['tag_angle'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("tag_angle()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns tag angle (deg)");
 this.setHelpUrl("");
  }
};


Blockly.Blocks['get_image'] = {
  init: function() {
    this.appendDummyInput()
        .appendField("getImage()");
    this.setOutput(true, null);
    this.setColour(0);
 this.setTooltip("returns a image (img)");
 this.setHelpUrl("");
  }
};

Blockly.Blocks['face_detection'] = {
  init: function() {
    this.appendValueInput("img")
        .appendField("face_detection()");
    this.setOutput(true, null);
    //this.setInputsInline(true);
    //this.setPreviousStatement(true, null);
    //this.setNextStatement(true, null);
    this.setColour(0);
 this.setTooltip("Img");
 this.setHelpUrl("");
  }
};
