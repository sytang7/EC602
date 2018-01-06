// Copyright © 2017 Siyuan Tang sytang7@bu.edu


#include <iostream>
#include <ctime>
#include <chrono>
#include <cmath>

using namespace std;
using namespace chrono;

int main(){
	/*
	uint8_t i = 1;
	auto start_clock = high_resolution_clock::now();
	while(i)
	{
		i++;
	}
	auto diff = high_resolution_clock::now() - start_clock;
	auto t = duration_cast<nanoseconds> (diff);
	cout << "estimated int8 time (nanoseconds): " << t.count()<< endl;
	*/

	clock_t start, end;
	uint16_t j = 1;
	start = clock();
	while(j)
	{
		j++;
	}
	end = clock();
	double microsecond = static_cast<double>(end - start);
	double nanosecond = microsecond / pow(2,8) * 1e3;
	cout << "estimated int8 time (nanoseconds): " << nanosecond <<endl;
	cout << "measured int16 time (microseconds): " << microsecond <<endl;


	/*uint32_t k = 1;
	start = clock();
	while(k)
	{
		k++;
	}
	end = clock();
	double second = static_cast<double>(end - start)/ CLOCKS_PER_SEC;
	*/
	double second = microsecond * pow(2,16) / 1e6;
	cout << "estimated int32 time (seconds): " << second <<endl;

	double year;
	year = second * pow(2,32) / 31536000;
	
	/*uint64_t q = 1;
	start = clock();
	while(q)
	{
		q++;
	}
	end = clock();
	double year = static_cast<double>(end - start)/ (CLOCKS_PER_SEC*31536000);
	*/
	cout << "estimated int64 time (years): " << year <<endl;
}