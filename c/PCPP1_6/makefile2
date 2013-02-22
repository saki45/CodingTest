allExec = ArrayTest stringTest VectorTest MyCircleTest

all	:
	make	$(allExec)

stringTest	:	stringTest.o
	g++	-o	stringTest	stringTest.o
stringTest.o	:	stringTest.cpp
	g++	-c	stringTest.cpp

ArrayTest	:	ArrayTest.o
	g++	-o	ArrayTest	ArrayTest.o
ArrayTest.o	:	ArrayTest.cpp
	g++	-c	ArrayTest.cpp

VectorTest	:	VectorTest.o
	g++	-o	VectorTest	VectorTest.o
VectorTest.o	:	VectorTest.cpp
	g++	-c	VectorTest.cpp

MyCircleTest	:	MyCircleTest.o	MyCircle.o
	g++	-o	MyCircleTest	MyCircleTest.o	MyCircle.o
MyCircle.o	:	MyCircle.h	MyCircle.cpp
	g++	-c	MyCircle.cpp
MyCircleTest.o	:	MyCircle.h	MyCircleTest.cpp
	g++	-c	MyCircleTest.cpp

.PHONY:	clean	
clean	:
	-rm	*.o
	-rm	$(allExec)
