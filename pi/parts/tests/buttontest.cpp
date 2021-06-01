#include "pinsetup.h"
#include "button.h"
#include "led.h"
#include <iostream>

int cont = 1;

int modeMax = 3;
int mode = 1;

int main(void){
	piStart();
	Led led(17);
	Button modeButton(23);
	Button powerButton(24);
	led.off();
	while(cont){
		std::cout << "hi" << "\n";
		if (powerButton.pressed()){
			cont = 0;
		}
		
		if (modeButton.pressed()){
			mode = mode%modeMax + 1;
			std::cout << "mode: " << mode << "\n";
			if (mode == 1){
				led.on();
			}
			else if (mode == 2){
				led.blink(3);
			}
			else{
				led.off();
			}
		}
	}
	return 0;
}
