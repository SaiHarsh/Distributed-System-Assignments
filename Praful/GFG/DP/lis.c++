#include <bits/stdc++.h>
using namespace std;
int maxx(int l[], int n)
{
	int i, s = 0;
	for (i = 0; i < n; i++)
	{
		if (s < l[i])
			s = l[i];
	}
	return s;
}

int lis (int a[], int n) 
{
	int l[n], i, j;
	for (i = 0; i < n; i++)
		l[i] = 1;

	for (i = 0; i < n; i++)
	{
		for (j = 0; j < i; j++)
		{
			if (a[i] > a[j])
				l[i] = l[j] + 1;
		}
//cout << i << endl;
	}

	return maxx(l, n) + 1;
}

int main()
{
	int t, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		int a[n], i;
		for (i = 0; i < n; i++)
			cin >> a[i];
		cout << lis(a, n) << endl;
	}
	return 0;
}
