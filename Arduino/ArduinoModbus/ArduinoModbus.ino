#include "Arduino.h"
#include "Modbus.h"
#include "ModbusSerial.h"

const int LED_COIL=13;
const int LEDPin=13;
ModbusSerial mb;

void setup() {
  // put your setup code here, to run once:
//Config Modbus Serial(port,speed,byte format)
mb.config(&Serial,9600,SERIAL_8N1);
//slave ID 1-247
mb.setSlaveId(1);
mb.addCoil(LED_COIL,false);
pinMode(LEDPin,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
mb.task();
digitalWrite(LEDPin,mb.Coil(LED_COIL));
}
