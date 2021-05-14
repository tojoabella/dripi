#include "pinsetup.h"

void pinSetup(){
	wiringPiSetupGpio();
}

void pinAssign(int pin, char *s){	
	if(!strcmp(s, "button")){
		pinMode(pin, INPUT);
		pullUpDnControl(pin, PUD_DOWN);
	}
	else if(!strcmp(s, "led")){
		pinMode(pin, OUTPUT);
	}
}
