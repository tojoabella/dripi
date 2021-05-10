#include "pinsetup.h"

void pinSetup(){
	wiringPiSetupGpio();
}

void pinAssign(int pin, char *s){	
	if(!strcmp(s, "button")){
		pinMode(pin, INPUT);
	}
	else if(!strcmp(s, "led")){
		pinMode(pin, OUTPUT);
	}
}
