#include "../pinsetup.h"
#include <signal.h>
#include <stdio.h>

static int cont = 1;

#define led 17
#define button 23
#define buttonPower 24

int modeMax = 3;
int mode = 1;

int buttonState = 0;
int lastReading = 0;
int currentReading = 0;
long timeChanged;
long timePress = 50;

void setup(){
	pinSetup();
	pinAssign(led, "led");
	pinAssign(button, "button");
}

void cleanup(int sig){
	cont = 0;
	pinMode(led, INPUT);
}

void ledOn(){
	digitalWrite(led, 1);
}

void ledBlink(){
	for (int i =  0; i < 3; i++){
		digitalWrite(led, 0);
		delay(200);
		digitalWrite(led, 1);
		delay(200);
	}
}

void ledOff(){
	digitalWrite(led, 0);
}

void powerCheck(){
	if (digitalRead(buttonPower)){
		cleanup(2);
	}
}

int main(void){
 	signal(SIGINT, cleanup);
	setup();
	ledOn();
	while(cont){
		powerCheck();
		
		currentReading = digitalRead(button);
		if(currentReading != lastReading){
			timeChanged = millis();
		}
		if(millis() - timeChanged > 50){
			if (currentReading != buttonState){
				buttonState = currentReading;
				if (buttonState){
					mode = mode%modeMax + 1;
					printf("mode: %d\n", mode);
					if (mode == 1){
						ledOn();
					}
					else if (mode == 2){
						ledBlink();
					}
					else{
						ledOff();
					}
				}
			}
		}
		lastReading = currentReading;
	}

	return 0;
}
