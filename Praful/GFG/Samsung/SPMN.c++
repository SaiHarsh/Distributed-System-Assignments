#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n;
	cin >> t;
	while (t--)
	{
		cin >> n;
		int a[n], b[1000], i;
		for (i = 0; i < 1000; i++)
			b[i] = 0;
		for (i = 0; i < n; i++)
		{
			cin >> a[i];
			if (a[i] >= 0)
				b[a[i]] = 1;
		}
		for (i = 1; i < 1000; i++)
		{
			if (b[i] == 0)
			{
				cout << i << endl;
				break;
			}
		}
	}
}
