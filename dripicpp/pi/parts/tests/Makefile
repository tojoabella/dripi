VPATH = ../..:..:$(OBJDIR)

HOMEDIR = ../../..
OBJDIR = $(HOMEDIR)/build

CC = g++-9.1
CXX = g++-9.1
INCLUDES = -I../.. -I..
CXXFLAGS = -g -Wall $(INCLUDES)
LDLIBS = -lwiringPi

TARGETS = $(HOMEDIR)/buttontest 

.PHONY: default
default: $(TARGETS)

$(HOMEDIR)/buttontest: buttontest.o pinsetup.o button.o led.o
	$(CXX) $(LDFLAGS) $^ $(LDLIBS) -o $@

$(OBJDIR)/buttontest.o: buttontest.cpp pinsetup.h button.h led.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<
