#include "led.h"
#include "pinsetup.h"
#include <wiringPi.h>

Led::Led(int _pinNum){
	pinNum = _pinNum;
	pinAssign(pinNum, "led");
	//pisetup::pinAssign(pinNum, "led");
}

Led::~Led(){
	pinMode(pinNum, INPUT);
}

void Led::on() const{
	digitalWrite(pinNum, 1);
}

void Led::off() const{
	digitalWrite(pinNum, 0);
}

void Led::blink(int count) const{
	for (int i = 0; i < count; i++){
		on();
		delay(200);
		off();
	}
}
