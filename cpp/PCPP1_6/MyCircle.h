class MyCircle {

public:
	MyCircle();
	MyCircle(int radius);

	//~MyCircle();

	int changeRadius(int radius);
	void printArea();

private:
	int _r;
};
