#include "pinsetup.h"
#include <signal.h>
#include <stdio.h>

#define ledPin 17
static int cont = 1;

void setup(){
	pinSetup();
	pinAssign(ledPin, "led");
}

void cleanup(int sig){
	cont = 0;
	pinMode(ledPin, INPUT);
}

int main(void){
	signal(SIGINT, cleanup);
	setup();	
	while(cont){
		digitalWrite(ledPin, HIGH);  //Make GPIO output HIGH level
		printf("led turned on >>>\n");		//Output information on terminal
		delay(1000);						//Wait for 1 second
		digitalWrite(ledPin, LOW);  //Make GPIO output LOW level
		printf("led turned off <<<\n");		//Output information on terminal
		delay(1000);						//Wait for 1 second
	}
	return 0;
}
