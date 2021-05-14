#include "../pinsetup.h"
#include <signal.h>
#include <stdio.h>

static int cont = 1;

#define led 17
#define button 23

void setup(){
	pinSetup();
	pinAssign(led, "led");
	pinAssign(button, "button");
}

void cleanup(int sig){
	cont = 0;
	pinMode(led, INPUT);
}

int main(void){
	signal(SIGINT, cleanup);
	setup();

	while(cont){
		if (digitalRead(button)){
			digitalWrite(led, 1);
			delay(1000);
			digitalWrite(led, 0);
			delay(1000);
		}
	}
	return 0;
}
