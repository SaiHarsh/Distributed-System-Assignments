#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t, n, i;
	cin >> t;
	while (t--)
	{
		cin >> n;
		string s;
		int a[30];
		memset (a, 0, sizeof (a));
		cin >> s;
		for (i = 0; i < n; i++){
			a[int(s[i])-97] += 1;
		}
		int f;
		f = 0;
		for (i = 0; i < n; i++)
		{
			if (a[int(s[i]) - 97] == 1)
			{
				f = 1;
				break;
			}
		}
		if (f == 1)
			cout << s[i] << endl;
		else 
			cout << "-1" << endl;
	
	}
	return 0;
}
