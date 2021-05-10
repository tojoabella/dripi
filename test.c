#include "pinsetup.h"
#include <signal.h>
#include <stdio.h>

static int cont = 1;

void cleanup(int sig){
	cont = 0;
	pinMode(ledPin, INPUT);
}

int main(void){
	signal(SIGINT, cleanup);
	printf("Program is starting ... \n");	
	pinSetup();
	pinAssign(ledPin, "led");	
	printf("Using pin%d\n",ledPin);	//Output information on terminal
	
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
