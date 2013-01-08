#include"MyCircle.h"

int main() {
	MyCircle c1;
	MyCircle c2(10);

	c1.printArea();
	c1.changeRadius(1);
	c1.printArea();

	c2.printArea();

	return 0;
}
