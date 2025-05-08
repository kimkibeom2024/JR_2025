#include <Servo.h>

Servo helmetServo;
const int servoPin = 9;  // 서보모터 핀

void setup() {
  helmetServo.attach(servoPin);
  helmetServo.write(0); // 초기 각도 설정
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'O') {
      helmetServo.write(90);  // 헬멧 착용 (정상)
    } else if (command == 'X') {
      helmetServo.write(0);   // 헬멧 미착용 (경고)
    }
  }
}