#include "pinsetup.h"
#include <wiringPi.h>

void piStart(){
	wiringPiSetupGpio();
}

void pinAssign(int pin, std::string s){	
	if(s == "button"){
		pinMode(pin, INPUT);
		pullUpDnControl(pin, PUD_DOWN);
	}
	else if(s == "led"){
		pinMode(pin, OUTPUT);
	}
}
