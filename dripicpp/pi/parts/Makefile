VPATH = ..

CC = g++-9.1
CXX = g++-9.1
INCLUDES = -I..
CXXFLAGS = -g -Wall $(INCLUDES)

HOMEDIR = ../..
OBJDIR = $(HOMEDIR)/build
TARGETS = $(OBJDIR)/button.o $(OBJDIR)/led.o

.PHONY: default
default: $(TARGETS)

$(OBJDIR)/button.o: button.cpp button.h pinsetup.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<

$(OBJDIR)/led.o: led.cpp led.h pinsetup.h
	$(CXX) $(CXXFLAGS) -c -o $@ $<
