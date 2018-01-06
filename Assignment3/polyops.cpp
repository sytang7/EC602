// Copyright © 2017 Siyuan Tang sytang7@bu.edu
typedef vector<double> Poly;

Poly add_poly(const Poly &a, const Poly &b)
{
	Poly res;

	int size = max(a.size(),b.size());

	if(a.size() == b.size())
		for(int i = 0;i < size;i ++)
			res.push_back(a[i]+b[i]);
	else for(int i = 0;i < size;i ++){
			if(i >= a.size())
				res.push_back(b[i]);
			else if(i >= b.size())
				res.push_back(a[i]);
			else res.push_back(a[i]+b[i]);
		}

	while(res.back() == 0.0)
	{
		res.pop_back();
		if(res.size() == 1)
			break;
	}

	return res;
}

Poly multiply_poly(const Poly &a,const Poly &b)
{
	int size = a.size() + b.size();
	Poly res(size - 1,0);
	for(int i = 0;i < a.size();i++)
		for(int j = 0;j < b.size();j++)
			res[i+j] += (a[i] * b[j]);


	while(res.back() == 0.0)
	{
		res.pop_back();
		if(res.size() == 1)
			break;
	}
	
	return res;	
}