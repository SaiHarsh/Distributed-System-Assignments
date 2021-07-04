#include <bits/stdc++.h>
using namespace std;
#define f(x) cin >> x
#define p(x) printf ("%d \n", x)
int lcs (string x, string y, int n, int m)
{
	int l[n+1][m+1];
	int i, j;
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= m; j++)
		{
			if (i == 0 || j == 0)
				l[i][j] = 0;

			else if (x[i-1] == y[j-1])
				l[i][j] = l[i-1][j-1] + 1;
			else 
				l[i][j] = max(l[i-1][j], l[i][j-1]);

		}
	}
	return l[n][m];
}
int main()
{
	int t;
	f(t);
	while (t--)
	{
		int n, m, i;
		f(n);f(m);
		string s1, s2;
		f(s1); f(s2);
		p(lcs(s1, s2, n, m));
	}
	return 0;
}
