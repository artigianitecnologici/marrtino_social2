#include <DynamixelSDK.h>

#define BAUDRATE 1000000 // Initial Baudrate
#define DEVICENAME "3" // Serial3 (485 EXP BOARD)
#define BUFFER_SIZE 1024

dynamixel::PortHandler *portHandler = dynamixel::PortHandler::getPortHandler(DEVICENAME);

uint8_t buffer[BUFFER_SIZE];

void setup() {
  Serial.begin(115200); // Serial (USB)
  portHandler = dynamixel::PortHandler::getPortHandler(DEVICENAME);
  portHandler->openPort();
  portHandler->setBaudRate(BAUDRATE);
}

void loop() {
  // Updates Baudrate
  //if (Serial.getBaudRate() != portHandler->getBaudRate()) {
  //  portHandler->setBaudRate(Serial.getBaudRate());
  //}
  
  int cb;

  // DXL -> USB
  cb = portHandler->readPort(buffer, BUFFER_SIZE);
  if (cb) {
    Serial.write(buffer, cb);
  }

  // USB -> DXL
  cb = 0;
  while (Serial.available()) {
    buffer[cb++] = Serial.read();
  }
  if (cb) {
    portHandler->writePort(buffer, cb); 
  }
}
