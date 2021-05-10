#include "pinsetup.h"
#include <wiringPi.h>

void pinSetup(int pin){
	pinMode(pin, OUTPUT);	
}
