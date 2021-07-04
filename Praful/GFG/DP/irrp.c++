#include <bits/stdc++.h>
using namespace std;
int minn (int a, int b, int c)
{
	if (a <= b && a <= c)
		return a;
	if (b<=a && b <= c)
		return b;
	return c;
}
int lcs (string x, string y, int n, int m)
{
	int l[n+1][m+1];
	int i, j;
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= m; j++)
		{
			if (i == 0)
				l[i][j] = j;
			else if (j == 0)
				l[i][j] = i;

			else if (x[i-1] == y[j-1])
				l[i][j] = l[i-1][j-1];
			else{
				l[i][j] = 1 + min( min(l[i][j-1],l[i-1][j]),l[i-1][j-1]);
			}
		}
	}
	return l[n][m];
}
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n, m;
		string s1, s2;
		cin >> n >> m;
		cin >> s1 >> s2;
		//f(s1); f(s2);
		cout << (lcs(s1, s2, n, m));
	}
	return 0;
}

