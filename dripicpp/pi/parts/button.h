#ifndef BUTTON_H
#define BUTTON_H

class Button{
	public:
		Button(int);

		bool pressed() const;
		bool waitForPress() const;
	private:
		int pinNum;
};

#endif
