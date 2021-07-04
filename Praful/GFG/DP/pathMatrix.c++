#include "use.h"
 int n;

int mat (int a[][100])
{
	int i, j;
	int l[n+1][n+1];
	for (i = 0; i <= n; i++)
	{
		for (j = 0; j <= n; j++)
		{
			if (i == 0 || j == 0)
				l[i][j] = 0;
			else if (a[i][j] >= a[i-1][j-1])
				l[i][j] = a[i][j];
			else 
				l[i][j] = max(max(l[i+1][j-1], l[i+1][j]), l[i+1][j+1]);
		}
	}
	return l[n][n];
}

int main()
{
	int t;
	s(t);
	while (t--)
	{
		int i, j;
		s(n);
		int a[100][100];
		f(i, 0, n)
		{
			f(j, 0, n)
			s(a[i][j]);
		}
		p(mat(a));
	}
	return 0;
}
