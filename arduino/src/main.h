#include "Arduino.h"

// Define the motor control pins
#define LEFT_MOTOR_PIN2 4//D2
#define LEFT_MOTOR_PIN1 0//D3
#define RIGHT_MOTOR_PIN2 13//D7
#define RIGHT_MOTOR_PIN1 12//D6

// Define the motor speed control pins (PWM)
#define LEFT_MOTOR_SPEED_PIN 2//D4
#define RIGHT_MOTOR_SPEED_PIN 14//D5

extern bool isStoped;
extern int motorSpeed;