#include "main.h"
#include "motorFunction.h"
void(* resetFunc) (void) = 0; //declare reset function @ address 0
void useGameData(char type, int value) {
  yield();
  switch (type) {
    case 'R':
      stopMotors();
      resetFunc();
      delay(10);
      break;
    case 'M':
      switch(value){
        case 1:
          moveForward(motorSpeed);
          break;
        case 0:
          stopMotors();
          break;
      }
      break;
    case 'L':
      switch(value){
        case 1:
          digitalWrite(LED_BUILTIN,0);
          break;
        case 0:
          digitalWrite(LED_BUILTIN,1);
          break;
      }
      break;
    //A Button
    case 'a':
      switch (value) {  //use switch statements if you aren't printing to Serial.
        case 1:
          Serial.println("A on");
          if(isStoped){
            moveForward(motorSpeed);
          }
          else{
            stopMotors();
          }
          // isStoped = !isStoped;
          // digitalWrite(LED, LOW);
          break;
        case 0:
          Serial.println("A off");
          // digitalWrite(LED, HIGH);
          break;
      }
      break;
    //B Button
    case 'p':
     switch (value) {  //use switch statements if you aren't printing to Serial.
        case 1:
          Serial.println("B on");
          break;
        case 0:
          Serial.println("B off");
          break;
      }
      break;
    //Y button
    case 'o':
      switch (value) {  //use switch statements if you aren't printing to Serial.
        case 1:
          Serial.println("Y on");
          break;
        case 0:
          Serial.println("Y off");
          break;
      }
      break;

    //You can do this for the other buttons...but I don't have to because its boring :)

    //X Button
    case 'i':
     switch (value) {  //use switch statements if you aren't printing to Serial.
        case 1:
          Serial.println("X on");
          break;
        case 0:
          Serial.println("X off");
          break;
      }
      break;

    //-------------Dpad Buttons------------//
    case 'd':
      switch (value) {
        //Dpad Center Button
        case 0:
          moveForward(motorSpeed);
          Serial.println("D-pad Center");
          break;
        //Dpad Left Button
        case 1:
          turnLeft(motorSpeed);
          Serial.println("D-pad Left");
          break;
        //Dpad Up Button
        case 2:
          moveForward(255);
          Serial.println("D-pad Up");
          break;
        //Dpad Right Button
        case 3:
          turnRight(motorSpeed);
          Serial.println("D-pad Right");
          break;
        //Dpad Down Button
        case 4:
          moveBackward(motorSpeed);
          Serial.println("D-pad Down");
          break;
      }
      break;


    //-------------Function Buttons------------//
    //Back Button
    case 'y':
      break;
    //Start Button
    case 'u':
      break;

    //-------------Joystick Buttons------------//
    //Left Joystick Button
    case 't':
      break;
    //Right Joystick Button
    case 'j':
      break;

    //-------------Trigger Buttons------------//
    //Top left trigger Button
    case 'w':
      break;
    //Top right trigger Button
    case 'e':
      Serial.println("slow mode");
      changeSpeed(80);
      motorSpeed = 80;
      break;
    //Bottom left Trigger(Some controllers have this as analog so 355 means on)
    case 'q':
      switch (value) {
        //        case 355:
        //          digitalWrite(LED, LOW);
        //          break;
        //        case 0:
        //          digitalWrite(LED, HIGH);
        //          break;
        default:
          //analog stuff handled here
          break;
      }
      break;
    //Bottom Right Trigger(Some controllers have this as analog so 355 means on)
    case 'r':
      Serial.println("r_trigger!");
      motorSpeed = map(value,0, 255, 100, 255);
    //   motorSpeed = value;
      Serial.print("speed: ");
      Serial.println(motorSpeed);
      changeSpeed(motorSpeed);
      switch (value) {
        
        //        case 355:
        //          digitalWrite(LED, LOW);
        //          break;
        //        case 0:
        //          digitalWrite(LED, HIGH);
        //          break;
        default:
          //analog stuff handled here
          break;
      }
      break;


    //-------------Analog------------//
    //Analog values(Joysticks) are under construction.  There's an annoying method i have to deal with in Android
    //(Every joystick movement is sent out to the esp8266 which causes too many packets to reset the esp).
    /*The range for these values is 100-355.  I chose these ranges because Android can't sent UDP packets of different length. I
      wanted a range of 0-255, so I simply bumped it up by adding 100. And it works great and smoothly for Android*/

    //left joystick X direction
    case 'k':
      // analogWrite(LED, value - 100);  /*Subtract by 100 since the incoming data has a range from 100-355, and Arduino's analogWrite() only accepts 0-255*/
      break;
    //left joystick Y direction
    case 'l':
      // analogWrite(LED_2, value - 100);
      break;
    //Right joystick X direction
    case 'z':
      break;
    //Right joystick Y direction
    case 'x':
      break;

    default:
      // moveForward(speed);
      break;

  }
  yield();
}