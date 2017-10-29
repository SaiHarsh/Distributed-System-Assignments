#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n;
	scanf ("%d",&t);
	int q = 0;
	while (t--)
	{
		string s;
		cin >> s;
		int l, i;
		i = s.size();
		int k = i;
		while i >= 0 {
			l = int(s.substr(0,i)+s.substr(i+1,k));
			if (l%6 == 0)
			{
				if (q<l)
					q = l;
			}
			i -= 1;
	}
		if (q == 0)
			printf ("-1 \n");
		else if (q == int(s.substr(0,1)))
			printf ("%s \n",s.substr(0,1));
		else
			printf ("%s \n",s);
	}
}

	

