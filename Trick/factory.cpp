#include<bits/stdc++.h>

using namespace std;

int main()
{
	int n;
	cin>>n;

	vector<vector<int> > arr(n, vector<int> (3));


	for(int i = 0; i<n;i++)
	{
		for(int j=0 ; j<3 ; j++)
		{
			cin>>arr[i][j];
		}
	}


	int dp[3][n];

	dp[0][0] = arr[0][0];
	dp[1][0] = arr[0][1];
	dp[2][0] = arr[0][2];

for(int i=1 ; i<n; i++)
{
	for(int j=0 ; j < 3 ; j++)
	{
		if(j==0)
		{
			dp[0][i] = max(dp[1][i-1]+ arr[i][0] , dp[2][i-1] + arr[i][0]);
		}


		if(j==1)
		{
			dp[1][i] = max(dp[0][i-1] + arr[i][1] , dp[2][i-1] + arr[i][1]);

		}

		if(j==2)
		{
			dp[2][i] = max(dp[0][i-1] + arr[i][2] , dp[1][i-1] + arr[i][2]);

		}


	}
}



cout<<max(dp[0][n-1],max(dp[1][n-1],dp[2][n-1]))<<"\n";


}