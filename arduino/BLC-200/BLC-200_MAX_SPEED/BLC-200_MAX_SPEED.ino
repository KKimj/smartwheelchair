#include "mas001.h"
#include "blc200.h"

/*****************************************************************************/
// User Configuration
#define DEVICE_ID 0
#define SPD_SETTIME 1 // // Caution! Speed set time is (0.1*SPD_SETTIME) second
/*****************************************************************************/

MAS001 myShield;
BLC200 myDevice(9600, 100); // Baudrate = 9600, Serial timeout = 100ms

int rated_speed;
int spd_input;
void setup() {
  Serial.begin(115200);

  
  // [[ Read rated speed from driver ]]
  // Serial.print("Read rated speed [RPM] : ");
  if(myDevice.get_Feedback(DEVICE_ID, 0xA6)){
    rated_speed = (uint16_t)myDevice.blcData[1] << 8 | (uint16_t)myDevice.blcData[2];
    // Serial.println(rated_speed);
  }else{
    Serial.println("Fail..");
    while(1);
  }
  while(!Serial.available());
  Serial.print("Press any KEY to start .. ");
  char tmp = Serial.read();
}

void loop() {
  spd_input = rated_speed;
  myDevice.set_SpeedWithTime(DEVICE_ID, 0, spd_input * 10, SPD_SETTIME);

  delay(100); // 0.1 sec
  
  myDevice.set_SpeedWithTime(DEVICE_ID, 0, 0, SPD_SETTIME);
  while(1);
}
