#include<iostream>
#include<cstring>
#include<string>

using namespace std;

int main() {
	int errors = 0;
	const char *pc = "a very long literal string";

	for(int ix = 0; ix < 10000000; ++ix) {
		int len = strlen(pc);
		char *pc2 = new char[len + 1];
		strcpy(pc2, pc);
		if(strcmp (pc2, pc)) {
			++errors;
		}

		delete[] pc2;
	}
	//printf("%d", errors);

	cout<<"C-Style: "<< errors << " errors occurred.\n"; 
	
	errors = 0;
	string str("a very long literal string");

	for(int ix = 0; ix < 10000000; ++ix) {
		int len = str.size();
		string str2 = str;
		if(str != str2) {
			++errors;
		}
	}
	
	cout<<"String-Style: "<< errors << " errors occurred." << endl;
	
	return 0;
}
	
