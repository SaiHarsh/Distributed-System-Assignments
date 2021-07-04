#include "use.h"
int partition(int a[], int n, int s, int k)
{
	if ( n < 0 )
		return abs (s-k);

	return min(partition (a, n-1, s+a[n], k), partition(a, n-1, s, k+a[n]));
}

int main()
{
	int t, n, i;
	s(n);
	int a[n];
	for (i = 0; i < n; i++)
		s(a[i]);
	p(partition (a, n-1, 0, 0));
	return 0;
}
