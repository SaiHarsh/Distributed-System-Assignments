#include <bits/stdc++.h>
using namespace std;
long getProb(long n)
{

int main()
{
	int t;
	scanf ("%d",&t);
	while (t--)
	{
		long int n;
		scanf ("%ld", &n);
		printf ("%ld \n", getProb(n));
	}
	return 0;
}
