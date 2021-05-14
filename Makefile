VPATH = pi:build

CC = gcc
INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

####################

TARGETS = pinsetup test buttontest
OBJDIR = ./build

####################

.PHONY: default
default: $(TARGETS)


pinsetup:
	$(MAKE) -C ./pi


test: $(OBJDIR)/test.o $(OBJDIR)/pinsetup.o

$(OBJDIR)/test.o: test.c pinsetup.h
	$(CC) $(CFLAGS) -c -o $@ $<


buttontest:
	$(MAKE) -C ./pi/parts


####################

.PHONY: cleanobjects
cleanobjects:
	rm -f *.o

.PHONY: clean
clean:
	rm -f test buttontest ./build/*.o
