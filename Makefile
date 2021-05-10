CC = gcc

INCLUDES = 

CFLAGS = -g -Wall $(INCLUDES)

LDFLAGS = -g

LDLIBS = -lwiringPi

test: pinsetup.o

test.o: pinsetup.h

pinsetup.o: pinsetup.h

.PHONY: clean
clean:
	rm -f test *.o
