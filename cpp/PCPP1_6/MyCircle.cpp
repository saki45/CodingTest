#include"MyCircle.h"
#include<iostream>

using namespace std;

MyCircle::MyCircle() {

	this->_r = 0;

}


MyCircle::MyCircle(int radius) {

	this->_r = radius;

}

int MyCircle::changeRadius(int radius) {

	this->_r = radius;

}

void MyCircle::printArea() {

	double area = this->_r*this->_r*3.1416;
	cout<<"The area is:"<<area<<endl;
}
