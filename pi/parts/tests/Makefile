VPATH = ../..:..:$(OBJDIR)

HOMEDIR = ../../..
OBJDIR = $(HOMEDIR)/build

CC = gcc
INCLUDES = -I../.. -I..
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

TARGETS = $(HOMEDIR)/buttontest 

.PHONY: default
default: $(TARGETS)

$(HOMEDIR)/buttontest: buttontest.o pinsetup.o buttonpower.o
	$(CC) $(LDFLAGS) $^ $(LDLIBS) -o $@

$(OBJDIR)/buttontest.o: buttontest.c pinsetup.h buttonpower.h
	$(CC) $(CFLAGS) -c -o $@ $<
