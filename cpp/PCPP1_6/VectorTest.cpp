#include<iostream>
#include<vector>

using namespace std;

int main() {
	vector<int> vec(2);
	cout<<"size:"<< vec.size()<<endl;
	
	vector<int>::iterator iter = vec.begin();

	vec.push_back(5);
	cout<<*(vec.end())<<endl;
	vec.push_back(3);
	cout<<*(vec.end())<<endl;
	vec.push_back(7);
	cout<<*(vec.end())<<endl;
	vec.pop_back();
	cout<<*(vec.end())<<endl;

	iter = vec.begin();
	while(iter != vec.end()) {
		cout<<*(iter++)<<' ';
	}
	cout<<*(vec.end())<<endl;
	cout<<vec.size()<<endl;	

	return 0;
		
}
