#include "pi/pinsetup.h"
#include "led.h"
#include <stdio.h>
#include <wiringPi.h>

static int cont = 1;

Led led(17);

void cleanup(int sig){
	cont = 0;
}

int main(void){
	piStart();	
	while(cont){
		led.on();
		printf("led turned on >>>\n");		//Output information on terminal
		delay(1000);						//Wait for 1 second
		led.off();
		printf("led turned off <<<\n");		//Output information on terminal
		delay(1000);						//Wait for 1 second
	}
	return 0;
}
