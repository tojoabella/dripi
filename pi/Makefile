CC = gcc
INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

OBJDIR = ../build

$(OBJDIR)/pinsetup.o: pinsetup.c pinsetup.h
	$(CC) $(CFLAGS) -c -o $@ $<
