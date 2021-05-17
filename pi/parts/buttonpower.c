#include "buttonpower.h"
#include "../pinsetup.h"

extern int buttonPower;
extern void cleanup(int sig);
void powerCheck(){
	if (digitalRead(buttonPower)){
		cleanup(2);
	}
}
