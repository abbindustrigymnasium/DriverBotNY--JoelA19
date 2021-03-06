#include "EspMQTTClient.h"
//Install libraries PubSubClient and EspMQTTClient
#include <Servo.h>

Servo servo;

void onConnectionEstablished();

EspMQTTClient client(
  "PerDefault",           // Wifi ssid
  "8002800280",           // Wifi password
  "maqiatto.com",  // MQTT broker ip
  8883,             // MQTT broker port
  "joel.andersson@abbindustrigymnasium.se",            // MQTT username
  "Changes",       // MQTT password
  "Microdatowwewwr2311",          // Client name
  onConnectionEstablished, // Connection established callback
  true,             // Enable web updater
  true              // Enable debug messages
);


#define motorPinRightDir  0//D2
#define motorPinRightSpeed 5//D1

#define motorPinLeftDir 2
#define motorPinLeftSpeed 4

void setup() {
  servo.attach(14); //D5
  pinMode(motorPinRightDir, OUTPUT);
  pinMode(motorPinRightSpeed, OUTPUT);
  pinMode(motorPinLeftDir, OUTPUT);
  pinMode(motorPinLeftSpeed, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(115200);
  servo.write(0);

  delay(2000);
}

bool off = false;

void turn(int degrees) {


    servo.write(degrees);
    Serial.println("svänger åt så här många grader:");
    Serial.println(degrees);
  }


void drive(bool dir, int speed) {

  //Om du vill åka rakt fram eller bak
  servo.write(90);

  Serial.println("Åk!");

  Serial.println(speed);
  digitalWrite(motorPinLeftDir, dir);
  analogWrite(motorPinLeftSpeed, speed);

  digitalWrite(motorPinRightDir, dir);
  analogWrite(motorPinRightSpeed, speed);

  digitalWrite(LED_BUILTIN, dir);

}

void onConnectionEstablished()
{

  client.subscribe("joel.andersson@abbindustrigymnasium.se/drive", [] (const String & payload)
  
  
  {Serial.println(payload);

    char info = payload.charAt(0);
    int length = payload.length();
    String value = payload.substring(1, 4);  
    int speed = value.toInt();
    String othervalue = payload.substring(5, 7);
    int direction = othervalue.toInt();

    if (info == 'f' || info == 'b'  )
    {
      bool dir = false;
      if (info == 'f')
        dir = true;
      drive(dir, speed);
    }
    turn(direction);
    
    Serial.println(payload);
    Serial.println("Hej");
      });
  }



void loop() {


  // put your main code here, to run repeatedly:
  client.loop();
}