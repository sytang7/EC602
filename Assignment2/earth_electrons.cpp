
// Copyright © 2017 Siyuan Tang sytang7@bu.edu

#include <iostream>

using namespace std;

int main(){
	double Mass_Earth = 5.972e24;
	double Mass_Proton = 1.672e-27;
	double Proton = Mass_Earth / Mass_Proton;
	double Estimate_Electron =  Proton * 0.4 / 8e12;
	double Upper_bound = Proton * 0.5 / 8e12;
	double Lower_bound = (Proton * 5/14) / 8e12;

	cout << Estimate_Electron <<endl;
	cout << Lower_bound << endl;
	cout << Upper_bound << endl;
}