TARGETS = test buttontest

VPATH = pi

CC = gcc

INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)

LDFLAGS = -g

LDLIBS = -lwiringPi


.PHONY: default
default: $(TARGETS)

test: pinsetup.o

test.o: pinsetup.h

pinsetup.o: pinsetup.h


buttontest: pinsetup.o

buttontest.o: pinsetup.h	

.PHONY: clean
clean:
	rm -f *.o test buttontest

.PHONY: all
all: clean default
