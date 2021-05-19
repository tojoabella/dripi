VPATH = ../

CC = gcc
INCLUDES = -I..
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

OBJDIR = ../../build
HOMEDIR = ../..
TARGETS = $(OBJDIR)/buttonpower.o 

.PHONY: default
default: $(TARGETS)

$(OBJDIR)/buttonpower.o: buttonpower.c pinsetup.h buttonpower.h
	$(CC) $(CFLAGS) -c -o $@ $<
