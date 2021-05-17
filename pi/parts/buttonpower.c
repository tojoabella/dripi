#include "buttonpower.h"
#include "../pinsetup.h"

extern void cleanup(int sig);
void powerCheck(int buttonPower){
	if (digitalRead(buttonPower)){
		cleanup(2);
	}
}
