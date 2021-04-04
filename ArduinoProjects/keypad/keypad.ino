#include <Keypad.h>
#include "DHT.h"
#include<Wire.h>
#include<LiquidCrystal_I2C.h>

DHT dht;

const byte ROWS = 4; 
const byte COLS = 3; 
int time = 2000;
char hexaKeys[ROWS][COLS] = {
  {'1', '2', '3'},
  {'4', '5', '6'},
  {'7', '8', '9'},
  {'*', '0', '#'}
};

byte rowPins[ROWS] = {9, 8, 7, 6}; 
byte colPins[COLS] = {5, 4, 3, 2}; 
LiquidCrystal_I2C lcd(0x27, 16, 2);
Keypad customKeypad = Keypad(makeKeymap(hexaKeys), rowPins, colPins, ROWS, COLS); 

void setup(){
  Serial.begin(9600);
  dht.setup(10);
    lcd.init();
  lcd.begin(16,2);   // Inicjalizacja LCD 2x16
  
  lcd.setCursor(0,0); // Ustawienie kursora w pozycji 0,0 (pierwszy wiersz, pierwsza kolumna)
}
  
void loop(){
  char customKey = customKeypad.getKey();
  
  if (customKey){
    Serial.println(customKey);
   
  }
  switch(customKey){
    case '1':
      Serial.println("VolumeDown");
      lcd.backlight();
      lcd.print("VolumeDown");
      delay(100);
      lcd.clear();
      lcd.noBacklight();
      break;
     case '2':
       Serial.println("Rewind");
      lcd.backlight();
      lcd.print("Rewind");
      delay(100);
      lcd.clear();
      lcd.noBacklight();
       break;
     case '3':
       Serial.println("Forward");
      lcd.backlight();
      lcd.print("Forward");
      delay(100);
      lcd.clear();
      lcd.noBacklight();
       break;
     case 'A':
       Serial.println("VolumeUp");
      lcd.backlight();
      lcd.print("VolumeUp");
      delay(100);
      lcd.clear();
      lcd.noBacklight();
       break;
      case 'B':
        Serial.println("Play/Pause");
      lcd.backlight();
      lcd.print("Play/Pause");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case '6':
        Serial.println("Music");
              lcd.backlight();
      lcd.print("Music");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case '5':
        Serial.println("Next");
              lcd.backlight();
      lcd.print("Next");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case '4':
        Serial.println("Previous");
              lcd.backlight();
      lcd.print("Previous");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case 'C':
        Serial.println("Win");
              lcd.backlight();
      lcd.print("Shutdown");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case 'D':
        Serial.println("Sleep");
              lcd.backlight();
      lcd.print("Canceled");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
      case '7':
        Serial.println("CMD");
              lcd.backlight();
      lcd.print("Open CMD");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
        case '*':
        Serial.println("MUTED");
              lcd.backlight();
      lcd.print("Mute Discord");
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;
        case '8':
        Serial.println("Temp");
              lcd.backlight();
      lcd.print(dht.getTemperature());
      delay(time);
      lcd.clear();
      lcd.noBacklight();
        break;

  }
    
  
}
