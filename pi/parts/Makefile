VPATH = ../

CC = gcc
INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

OBJDIR = ../../build
HOMEDIR = ../..
TARGETS = $(HOMEDIR)/buttontest $(OBJDIR)/buttonpower.o 

.PHONY: default
default: $(TARGETS)

$(HOMEDIR)/buttontest: $(OBJDIR)/buttontest.o $(OBJDIR)/pinsetup.o $(OBJDIR)/buttonpower.o
	$(CC) $(LDFLAGS) $^ $(LDLIBS) -o $@

$(OBJDIR)/buttontest.o: buttontest.c pinsetup.h buttonpower.h
	$(CC) $(CFLAGS) -c -o $@ $<

$(OBJDIR)/buttonpower.o: buttonpower.c pinsetup.h buttonpower.h
	$(CC) $(CFLAGS) -c -o $@ $<
