CC = gcc

CFLAGS = -g -Wall

LDFLAGS = -lwiringPi

test:

test.o:

.PHONY: clean
clean:
	rm -f test *.o
