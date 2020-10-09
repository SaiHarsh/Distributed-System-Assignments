# include<bits/stdc++.h>

using namespace std;

int main(){
	int n;
	cin>>n;

	vector<int> arr(n);
    
    for(int i=0; i<n; i++) cin>>arr[i];

    int dp[n];
	dp[0] = 1;
 	
 	for(int i=1 ; i < n ; i++)
 	{
 		if(arr[i] > arr[i-1])
 		{
 			dp[i] = dp[i-1] +1;
 		}
 		else dp[i] = dp[i-1];
 	}

 	cout<<dp[n-1]<<"\n";


}