CXX := clang++
CXX_STD := -std=c++2b
CXX_FLAGS :=
INCLUDES := 

PROJECT_HOME := /Users/edmundlskoviak/Documents/repos/activity_playgroud
LIBS := -L/usr/local/lib -L/opt/homebrew/Cellar/libpq/16.0/lib -lpqxx -lpq

SRC := src
BUILD := build

SRCS := hello.cpp map.cpp tuple.cpp polymorph.cpp template.cpp

all : hello map tuple polymorph template fstream
	@echo Making all complete

testlibpqxx : $(SRC)/testlibpqxx.cpp
	$(CXX) $(CXX_STD) $(CXX_FLAGS) -o $(BUILD)/$@ $< -L/usr/local/lib -L/opt/homebrew/Cellar/libpq/16.0/lib -lpqxx -lpq
 
connect.o : $(SRC)/connect.cpp
	$(CXX) $(CXX_STD) $(CXX_FLAGS) -fPIC -c -o $(BUILD)/$@ $<

activity.o : $(SRC)/activity.cpp
	$(CXX) $(CXX_STD) $(CXX_FLAGS) -fPIC -c -o $(BUILD)/$@ $<

libactivity : $(BUILD)/connect.o $(BUILD)/activity.o
	$(CXX) -shared $(CXX_FLAGS) $(LIBS) -o $(BUILD)/libactivity.A.dylib $<

libtest : $(SRC)/test/libtest.cpp
	$(CXX) $(CXX_STD) $(CXX_FLAGS) -o $(BUILD)/$@ $< -L$(PROJECT_HOME)/$(BUILD) -lactivity

