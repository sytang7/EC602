// Copyright © 2017 Siyuan Tang. sytang7@bu.edu

#include <iostream>

using namespace std;


int main(int argumentcount, char** arguments)
{

	int i = 1;
	while(arguments[i]){
		if(i < 5)
			cout << arguments[i]<<endl;
		else{
			cerr << arguments[i]<<endl;
		}
		i++;
	}
}
