class EyeController {
  constructor(elements = {}, eyeSize = '33.33vmin') {
    this._eyeSize = eyeSize;
    this._blinkTimeoutID = null;

    this.setElements(elements);
  }

  get leftEye() { return this._leftEye; }
  get rightEye() { return this._rightEye; }

  setElements({
    leftEye,
    rightEye,
    upperLeftEyelid,
    upperRightEyelid,
    lowerLeftEyelid,
    lowerRightEyelid,
    upperLeftMouthlid,
    upperRightMouthlid,
  } = {}) {
    this._leftEye = leftEye;
    this._rightEye = rightEye;
    this._upperLeftEyelid = upperLeftEyelid;
    this._upperRightEyelid = upperRightEyelid;
    this._lowerLeftEyelid = lowerLeftEyelid;
    this._lowerRightEyelid = lowerRightEyelid;
    this._upperLeftMouthlid = upperLeftMouthlid;
    this._upperRightMouthlid = upperRightMouthlid;
    return this;
  }

  _createKeyframes ({
    tgtTranYVal = 0,
    tgtRotVal = 0,
    enteredOffset = 1/3,
    exitingOffset = 2/3,
  } = {}) {
    return [
      {transform: `translateY(0px) rotate(0deg)`, offset: 0.0},
      {transform: `translateY(${tgtTranYVal}) rotate(${tgtRotVal})`, offset: enteredOffset},
      {transform: `translateY(${tgtTranYVal}) rotate(${tgtRotVal})`, offset: exitingOffset},
      {transform: `translateY(0px) rotate(0deg)`, offset: 1.0},
    ];
  }

  express({
    type = '',
    // level = 3,  // 1: min, 5: max
    duration = 1000,
    enterDuration = 75,
    exitDuration = 75,
  }) {
    if (!this._leftEye) {  // assumes all elements are always set together
      console.warn('Eye elements are not set; return;');
      return;
    }

    const options = {
      duration: duration,
    };
    
  }

  blink({
    duration = 150,  // in ms
  } = {}) {
    if (!this._leftEye) {  // assumes all elements are always set together
      console.warn('Eye elements are not set; return;');
      return;
    }

    [this._leftEye, this._rightEye].map((eye) => {
      eye.animate([
        {transform: 'rotateX(0deg)'},
        {transform: 'rotateX(90deg)'},
        {transform: 'rotateX(0deg)'},
      ], {
        duration,
        iterations: 1,
      });
    });
  }

  startBlinking({
    maxInterval = 5000
  } = {}) {
    if (this._blinkTimeoutID) {
      console.warn(`Already blinking with timeoutID=${this._blinkTimeoutID}; return;`);
      return;
    }
    const blinkRandomly = (timeout) => {
      this._blinkTimeoutID = setTimeout(() => {
        this.blink();
        blinkRandomly(Math.random() * maxInterval);
      }, timeout);
    }
    blinkRandomly(Math.random() * maxInterval);
  }
  
  normal() {
	
	    document.getElementById("occhiodx").src = "image/face03/normal/occhio dx.png"; 
    	document.getElementById("occhiosx").src = "image/face03/normal/occhio sx.png"; 	
    	document.getElementById("bocca").src = "image/face03/normal/bocca.png"; 
    	document.getElementById("naso").src = "image/face03/normal/naso.png"; 
  }	 
  
  happy() {
	    document.getElementById("occhiodx").src = "image/face03/happy/occhio dx.png"; 
    	document.getElementById("occhiosx").src = "image/face03/happy/occhio sx.png"; 	
    	document.getElementById("bocca").src = "image/face03/happy/bocca.png"; 
    	document.getElementById("naso").src = "image/face03/happy/naso.png"; 
  }	 

  angry() {
	    document.getElementById("occhiodx").src = "image/face03/angry/occhio dx.png"; 
      document.getElementById("occhiosx").src = "image/face03/angry/occhio sx.png"; 	
      document.getElementById("bocca").src = "image/face03/angry/bocca.png"; 
      document.getElementById("naso").src = "image/face03/angry/naso.png";  
  }	 
  sad() {
	    
      document.getElementById("occhiodx").src = "image/face03/sad/occhio dx.png"; 
      document.getElementById("occhiosx").src = "image/face03/sad/occhio sx.png"; 	
      document.getElementById("bocca").src = "image/face03/sad/bocca.png"; 
      document.getElementById("naso").src = "image/face03/sad/naso.png"; 
  }	   
  surprise() {
    document.getElementById("occhiodx").src = "image/face03/surprise/occhio dx.png"; 
    document.getElementById("occhiosx").src = "image/face03/surprise/occhio sx.png"; 	
    document.getElementById("bocca").src = "image/face03/surprise/bocca.png"; 
    document.getElementById("naso").src = "image/face03/surprise/naso.png"; 
  }	  
  fear() {
    document.getElementById("occhiodx").src = "image/face03/fear/occhio dx.png"; 
    document.getElementById("occhiosx").src = "image/face03/fear/occhio sx.png"; 	
    document.getElementById("bocca").src = "image/face03/fear/bocca.png"; 
    document.getElementById("naso").src = "image/face03/fear/naso.png"; 
  }	  
  speak() {
    document.getElementById("bocca").src = "image/face02/talk3.gif"; 
    document.getElementById("naso").src = "image/nosetalkmarrtina1.gif"; 
  }	

  sings() {
    document.getElementById("bocca").src = "image/boccachecanta.gif"; 
    document.getElementById("naso").src = "image/nosetalkmarrtina1.gif"; 
  }  

  stopBlinking() {
    clearTimeout(this._blinkTimeoutID);
    this._blinkTimeoutID = null;
  }

  setEyePosition(eyeElem, x, y, isRight = false) {
    if (!eyeElem) {  // assumes all elements are always set together
      console.warn('Invalid inputs ', eyeElem, x, y, '; retuning');
      return;
    }

    if (!!x) {
      if (!isRight) {
        eyeElem.style.left = `calc(${this._eyeSize} / 3 * 2 * ${x})`;
      } else {
        eyeElem.style.right = `calc(${this._eyeSize} / 3 * 2 * ${1-x})`;
      }
    }
    if (!!y) {
      eyeElem.style.bottom = `calc(${this._eyeSize} / 3 * 2 * ${1-y})`;
    }
  }
}

const eyes = new EyeController({
  leftEye: document.querySelector('.left.bulb'),
  rightEye: document.querySelector('.right.bulb'),
  upperLeftEyelid: document.querySelector('.left .eyelid.upper'),
  upperRightEyelid: document.querySelector('.right .eyelid.upper'),
  lowerLeftEyelid: document.querySelector('.left .eyelid.lower'),
  lowerRightEyelid: document.querySelector('.right .eyelid.lower'),
  upperLeftMouthlid: document.querySelector('.mouthid.upper'),
  lowerLeftMouthlid: document.querySelector('.mouthid.lower'),
  
});

