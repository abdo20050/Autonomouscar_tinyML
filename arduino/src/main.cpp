#include "main.h"
#include "gamePadfunctions.h"
/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/Blink
*/
// the setup function runs once when you press reset or power the board
#define buffS 2
char buffer[buffS];

bool isStoped = true;
int motorSpeed = 100;

void setup()
{
  Serial.begin(115200);
  // initialize digital pin LED_BUILTIN as an output.
  Serial.println("hello Serial!");
  pinMode(LED_BUILTIN, OUTPUT);
  // Set the motor control pins as outputs
  pinMode(LEFT_MOTOR_PIN1, OUTPUT);
  pinMode(LEFT_MOTOR_PIN2, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN1, OUTPUT);
  pinMode(RIGHT_MOTOR_PIN2, OUTPUT);

  // Set the motor speed control pins as outputs
  pinMode(LEFT_MOTOR_SPEED_PIN, OUTPUT);
  pinMode(RIGHT_MOTOR_SPEED_PIN, OUTPUT);
  Serial.println("Wait RspPi!");
  bool ledS = 1;
  while (!Serial.available())
  {
    digitalWrite(LED_BUILTIN, ledS);
    Serial.print('.');
    delay(500);
    ledS = !ledS;
  }
  digitalWrite(LED_BUILTIN, 1);
}

// the loop function runs over and over again forever
void loop()
{
  if (Serial.available())
  {
    char InputType, InputValue;
    Serial.readBytes(buffer, buffS);
    InputType = buffer[0];
    if (isalpha(InputType))
    {
      InputValue = buffer[1];
      Serial.print(InputType);
      Serial.println(InputValue,DEC);
      useGameData(InputType, (int)InputValue);
    }
  }
  // delay(10);
  // Serial.println("ummm");
  // digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(1000);                      // wait for a second
  // digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  // delay(1000);                      // wait for a second
endloop:
  void pass();
}
