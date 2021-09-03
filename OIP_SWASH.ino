#include <Servo.h>
Servo servo;
int Status;
int delayy = 5000;
void setup() {
Serial.begin(9600);
servo.attach(10);
pinMode(8, OUTPUT); //WATERPUMP
pinMode(9, OUTPUT); //LEDLIGHT
pinMode(7, OUTPUT); //FAN
pinMode(12, OUTPUT); //platform
pinMode(11, INPUT);
  digitalWrite(7,HIGH);
  digitalWrite(8,HIGH); 
  digitalWrite(9,HIGH);  
  digitalWrite(12,LOW);  
}

void loop() {
  servo.write(0);
  delay(500);
  Platform_lowering();
  Waterpump();
  Camera_positioning(); 
  FAN_on();
  drainage_opening();   
  Platform_rising();
  UV();
  Camera_positioning();
  Collection();
}  
void Platform_lowering()
  {
  //************platform lowering******************//
  digitalWrite(12,HIGH);  
  delay(delayy);
  digitalWrite(12,LOW);
  }
void Waterpump()
  {
  d`igitalWrite(8,LOW);
  }
void ultrasonic_cleaner()
  {
  digitalWrite(8,HIGH);
  delay(delayy);
  delay(delayy);
  }
void FAN_on()
  {
  digitalWrite(7,HIGH);
  }  
void Platform_rising()
  {
  digitalWrite(12,HIGH);  
  delay(delayy);
  digitalWrite(12,LOW);    
  }
void drainage_opening() 
  {
   servo.write(540);   
  }  
void UV()
  {
    
  }
void Camera_positioning()
  {
  digitalWrite(12,HIGH);
  delay(50);
  digitalWrite(12,LOW);
  delay(delayy);
  digitalWrite(12,HIGH);
  delay(50);
  digitalWrite(12,LOW);
  delay(delayy);
  digitalWrite(12,HIGH);
  delay(50);
  digitalWrite(12,LOW);
  delay(delayy);
  digitalWrite(12,HIGH);
  delay(50);
  digitalWrite(12,LOW);
  delay(delayy);
  }
void UV_positioning()
  {
  digitalWrite(9,LOW); 
  }
void Collection()
  {
  digitalWrite(9,HIGH);
  digitalWrite(12,HIGH);
  delay(delayy);
  servo.write(0);
  digitalWrite(7,HIGH); 
  delay(delayy);
  delay(delayy);       
  }    
