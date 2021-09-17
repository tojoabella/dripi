#include "button.h"
#include "pinsetup.h"
#include <wiringPi.h>
#include <iostream>
Button::Button(int _pinNum){
	pinNum = _pinNum;
	pinAssign(pinNum, "button");
	//pisetup::pinAssign(pinNum, "button");
}

bool Button::pressed() const{
	int lastReading = 0;
	int currentReading = 0; 
	long unsigned timePress = 50;	
	long unsigned timeStart = millis();
	long unsigned timeEnd = timeStart + 2*timePress;
	while(millis() < timeEnd){
		currentReading = digitalRead(pinNum);
		if (currentReading != lastReading){
			return true;
		}
	}
	return false;
}



bool Button::waitForPress() const{
	int buttonState = 0;
        int lastReading = 0;
        int currentReading = 0;   
        long unsigned timeChanged = 0; 
        long unsigned timePress = 50;
	while(1){
		currentReading = digitalRead(pinNum);
		if (currentReading != lastReading){
			timeChanged = millis(); //millis is wiringpi
		}
		if (millis() - timeChanged > timePress){
			if (buttonState){
				return true;
			}
		}
	}
}

