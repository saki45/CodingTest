#include<stdio.h>
#include<cassert>

using namespace std;

int main(int argc, char* argv[]) {

	assert(1 == 1);

	printf("Hello world!\n");
	assert(1 == 0);
	return 0;
}
