VPATH = ../

CC = gcc
INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

OBJDIR = ../../build
HOMEDIR = ../..
TARGETS = $(HOMEDIR)/buttontest

.PHONY: default
default: $(TARGETS)

$(HOMEDIR)/buttontest: $(OBJDIR)/buttontest.o $(OBJDIR)/pinsetup.o
	$(CC) $(LDFLAGS) $^ $(LDLIBS) -o $@

$(OBJDIR)/buttontest.o: buttontest.c pinsetup.h	
	$(CC) $(CFLAGS) -c -o $@ $<
