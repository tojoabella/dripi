#ifndef LED_H
#define LED_H

class Led{
	public:
		Led(int);
		~Led();
		
		void on() const;
		void off() const;
		void blink(int) const;

	private:
		int pinNum;
};

#endif
