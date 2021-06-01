VPATH = pi:build:pi/parts

CC = g++-9.1
CXX = g++-9.1
INCLUDES = -I./pi/parts
CXXFLAGS = -g -Wall $(INCLUDES)
LDFLAGS = -g
LDLIBS = -lwiringPi

####################

#TARGETS = pinsetup piparts test
TARGETS = pisetup piparts tests
OBJDIR = ./build
EXECUTABLES = test buttontest

####################

.PHONY: default
default: $(TARGETS)

####################

pisetup:
	$(MAKE) -C ./pi

piparts:
	$(MAKE) -C ./pi/parts


#test: test.o build/pinsetup.o build/led.o

#$(OBJDIR)/test.o: test.cpp pinsetup.h led.h
#	$(CXX) $(CXXFLAGS) -c -o $@ $<

####################

.PHONY: clean
clean:
	rm -f $(EXECUTABLES) ./build/*.o

.PHONY: tests
tests:
	$(MAKE) -C ./pi/parts/tests
