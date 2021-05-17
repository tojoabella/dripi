VPATH = pi:build

CC = gcc
INCLUDES = 
CFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

####################

#TARGETS = pinsetup piparts test
TARGETS = pinsetup piparts test tests
OBJDIR = ./build

####################

.PHONY: default
default: $(TARGETS)

####################

pinsetup:
	$(MAKE) -C ./pi

piparts:
	$(MAKE) -C ./pi/parts


test: $(OBJDIR)/test.o $(OBJDIR)/pinsetup.o

$(OBJDIR)/test.o: test.c pinsetup.h
	$(CC) $(CFLAGS) -c -o $@ $<

####################

.PHONY: clean
clean:
	rm -f test buttontest ./build/*.o

.PHONY: tests
tests:
	$(MAKE) -C ./pi/parts/tests
