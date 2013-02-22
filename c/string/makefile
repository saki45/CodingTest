allExec =	stringRotateCheck stringRotateCheck2

all	:
	make	$(allExec)

stringRotateCheck	:	stringRotateCheck.o
	gcc	-o	stringRotateCheck	stringRotateCheck.o

stringRotateCheck2	:	stringRotateCheck2.o
	gcc	-o	stringRotateCheck2	stringRotateCheck2.o

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
