#include "main.h"

void moveForward(int speed) {
  Serial.println("move forward");
  isStoped = false;
  analogWrite(LEFT_MOTOR_SPEED_PIN, speed);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, speed);
  digitalWrite(LEFT_MOTOR_PIN1, HIGH);
  digitalWrite(LEFT_MOTOR_PIN2, LOW);
  digitalWrite(RIGHT_MOTOR_PIN1, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void moveBackward(int speed) {
  Serial.println("move backward");
  isStoped = false;
  analogWrite(LEFT_MOTOR_SPEED_PIN, speed);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, speed);
  digitalWrite(LEFT_MOTOR_PIN1, LOW);
  digitalWrite(LEFT_MOTOR_PIN2, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN1, LOW);
  digitalWrite(RIGHT_MOTOR_PIN2, HIGH);
}

void turnLeft(int speed) {
  Serial.println("Turn left");
  isStoped = false;
  analogWrite(LEFT_MOTOR_SPEED_PIN, speed);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, speed);
  digitalWrite(LEFT_MOTOR_PIN1, LOW);
  digitalWrite(LEFT_MOTOR_PIN2, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN1, HIGH);
  digitalWrite(RIGHT_MOTOR_PIN2, LOW);
}

void turnRight(int speed) {
  Serial.println("Turn right");
  isStoped = false;
  analogWrite(LEFT_MOTOR_SPEED_PIN, speed);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, speed);
  digitalWrite(LEFT_MOTOR_PIN1, HIGH);
  digitalWrite(LEFT_MOTOR_PIN2, LOW);
  digitalWrite(RIGHT_MOTOR_PIN1, LOW);
  digitalWrite(RIGHT_MOTOR_PIN2, HIGH);
}

void stopMotors() {
  analogWrite(LEFT_MOTOR_SPEED_PIN, 0);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, 0);
  digitalWrite(LEFT_MOTOR_PIN1, LOW);
  digitalWrite(LEFT_MOTOR_PIN2, LOW);
  digitalWrite(RIGHT_MOTOR_PIN1, LOW);
  digitalWrite(RIGHT_MOTOR_PIN2, LOW);
  isStoped = true;
}
void changeSpeed(int speed){
  analogWrite(LEFT_MOTOR_SPEED_PIN, speed);
  analogWrite(RIGHT_MOTOR_SPEED_PIN, speed);
}