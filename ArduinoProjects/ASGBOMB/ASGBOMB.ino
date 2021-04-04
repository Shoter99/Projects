#include<LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27, 16, 2);
#include <Keypad.h>



const byte ROWS = 4;
const byte COLS = 3;

bool started = false;
byte rowPins[ROWS] = {13,12,11,10};
byte colPins[COLS] = {9,8,7};

char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
Keypad kboard = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  kboard.setHoldTime(3);
  kboard.waitForKey();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  
  char key = kboard.getKey();  
  started = Start();
  if(started){
    Serial.print("Bomb started");
  }
  

}
bool Start(){
  char key = kboard.getKey();
  KeyState state = kboard.getState();
  if(state == HOLD && key == '#'){
    Serial.print("Hold");
    return true;
  }
  return false;
}
