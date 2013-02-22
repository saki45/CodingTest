allExec = ArrayTest stringTest VectorTest MyCircleTest

all	:
	make	$(allExec)

stringTest	:	stringTest.o
	g++	-o	stringTest	stringTest.o

ArrayTest	:	ArrayTest.o
	g++	-o	ArrayTest	ArrayTest.o

VectorTest	:	VectorTest.o
	g++	-o	VectorTest	VectorTest.o

MyCircleTest	:	MyCircleTest.o	MyCircle.o
	g++	-o	MyCircleTest	MyCircleTest.o	MyCircle.o
MyCircle.o	:	MyCircle.h	
MyCircleTest.o	:	MyCircle.h

.PHONY:	clean	
clean	:
	-rm	*.o
	-rm	$(allExec)
