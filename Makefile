CXX := clang++
CXX_STD := -std=c++2b
CXX_FLAGS :=
INCLUDES := 

LIBS := -lpqxx -lpq

SRC := src
BUILD := build

SRCS := hello.cpp map.cpp tuple.cpp polymorph.cpp template.cpp

all : hello map tuple polymorph template fstream
	@echo Making all complete

testlibpqxx : $(SRC)/testlibpqxx.cpp
	$(CXX) $(CXX_STD) $(CXX_FLAGS) -o $(BUILD)/$@ $< -L/usr/local/lib -L/opt/homebrew/Cellar/libpq/16.0/lib -lpqxx -lpq
 