#include "pinsetup.h"
#include "buttonpower.h"

void powerCheck(int buttonPower){
	if (digitalRead(buttonPower)){
		cleanup(2);
	}
}
