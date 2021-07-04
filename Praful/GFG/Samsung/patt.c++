#include <bits/stdc++.h>
using namespace std;
int check (string s, int i, int n)
{
	int j, flag;
	flag = 0;
	for (j = i+1; j < n; j++)
	{
		if (s[j] == '0')
		{
			flag = 1;
			continue;
		}
		if (s[j] == '1' && flag == 1)
			return j;
		else 
			return -1;
	}
	return -1;
}
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		string s;
		cin >> s;
		int n, i, k , c;
		n = s.length();
		c = 0; i = 0; 
		k = 0;
		while (i < n) 
		{
			if (s[i] == '1')
			{
				k = check (s, i, n);
				if (k != -1)
				{
					c += 1;
					i = k;
				}
				else 
					i += 1;
			}
			else 
				i += 1;
//cout << i << n << endl;
		}
		cout << c << endl;
	}
}
