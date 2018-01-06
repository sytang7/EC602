// Copyright © 2017 Siyuan Tang sytang7@bu.edu
#include <string>

using namespace std;

typedef string BigInt;

BigInt multiply_int(const BigInt &a, const BigInt &b)
{
	BigInt res(a.size() + b.size(), '0');
    
    for (int i = a.size() - 1; i >= 0;i--) {
        int carry = 0;
        for (int j = b.size() - 1; j >= 0;j--) {
            int tmp = (res[i + j + 1] - '0') + (a[i] - '0') * (b[j] - '0') + carry;
            res[i + j + 1] = tmp % 10 + '0';
            carry = tmp / 10;
        }
        res[i] += carry;
    }
    
    size_t start = res.find_first_not_of("0");
    if (string::npos != start) {
        return res.substr(start);
    }
    return "0";

/*
	int NUM = 6;
	Poly A(a.size(),0),B(b.size(),0);
	int size;
	size = a.size();
	for(int i= 0;i < size;i++)
		A[size - i - 1] = a[i] - 48;
	size = b.size();
	for(int i= 0;i < size;i++)
		B[size - i - 1] = b[i] - 48;

	Poly C = multiply_poly(A,B);

	long long tmp = 0;
	BigInt res;
	int count = NUM;
	for(int i = C.size()-1;i >= 0;i--)
	{
		tmp = tmp*10 + C[i];
		count --;

		if(count == 0 || i == 0)
		{
			if(i == 0)
				NUM = C.size()%NUM;
			if(res != "")
			{
				size = to_string(tmp).size() - NUM;
				BigInt str1 = res.substr(0 , res.size() - size - 1);
				BigInt str2 = res.substr(res.size() - size - 1);
				BigInt str3 = to_string(tmp).substr(0,size);
				BigInt str4 = to_string(tmp).substr(size);
				int x = 0,y = 0;
				for(int j = 0;j < str2.size();j++)
					x = x*10 + (str2[j] - '0');
				for(int j = 0;j < str3.size();j++)
					y = y*10 + (str3[j] - '0');

				BigInt mid = to_string(x+y);
				while(mid.size() < (size + 1))
					mid.insert(0,"0");

				str1 += mid;
				str1 += str4;

				res = str1;
			}
			else res = to_string(tmp);
			
			tmp = 0;
			count = NUM;
		}
	}

	return res;
	*/
}