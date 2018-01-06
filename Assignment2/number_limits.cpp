// Copyright © 2017 Siyuan Tang sytang7@bu.edu

#include <iostream>
#include <cstdio>
#include <cfloat>
#include <cmath>

using namespace std;

int main()
{
	long double Rs,Rm,Ri;
	int n,m;
	Rs = Rm = Ri = 0;

	n = 16;
	m = 10;
	Rs = 1/ pow(2,-14);
	Rm = (pow(2,n-1)*(2-pow(2,-m))) / INT16_MAX;
	Ri = INT16_MAX/pow(2,11);
	cout << "16 :Ri= "<<Ri << " Rm= "<<Rm << " Rs= "<< Rs <<endl;

	n = 32;
	m = 23;
	Rs = 1/ FLT_MIN;
	Rm = FLT_MAX / INT32_MAX;
	Ri = INT32_MAX/pow(2,24);
	cout << "32 :Ri= "<<Ri << " Rm= "<<Rm << " Rs= "<< Rs <<endl;

	n = 64;
	m = 52;
	Rs = 1/ DBL_MIN;
	Rm = DBL_MAX / INT64_MAX;
	Ri = INT64_MAX/pow(2,53);
	cout << "64 :Ri= "<<Ri << " Rm= "<<Rm << " Rs= "<< Rs <<endl;
}