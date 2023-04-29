int x;
#include<Servo.h>
Servo myThumb;
Servo myIndex;
Servo myMiddle;
void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  myThumb.attach(7);
  myMiddle.attach(8);
  myIndex.attach(12);
}

void loop() {
  int val;
  while (!Serial.available());
  x = Serial.readString().toInt();
  Serial.print(x + 1);
  val=x+1;
  if(val == 2) // All down
  {
    myThumb.write(180);
    myMiddle.write(0);
    myIndex.write(0);
    
  }
  else if(val == 3)//Middle Finger up
  {
    myThumb.write(180);
    myMiddle.write(180);
    myIndex.write(0);
    
  }
  else if(val == 4) //Index Finger up
  {
    myThumb.write(180);
    myMiddle.write(0);
    myIndex.write(180);
 
    
  }
  else if(val == 5) //Victory
  {
    myThumb.write(180);
    myMiddle.write(180);
    myIndex.write(180);
    
  }
  else if(val == 6)//Thumb
  {
    myThumb.write(0);
    myMiddle.write(0);
    myIndex.write(0);
    
  }
  else if(val == 7)//Ninety
  {
    myThumb.write(180);
    myMiddle.write(180);
    myIndex.write(0);
    
  }
  else if(val == 8)//Loser
  {
    myThumb.write(0);
    myMiddle.write(0);
    myIndex.write(180);
    
  }
  else if(val == 9)//All Up
  {
    myThumb.write(0);
    myMiddle.write(180);
    myIndex.write(180);
    
  }
 
  
}
