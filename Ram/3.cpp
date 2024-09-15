#include <bits/stdc++.h>
using namespace std;
int main()
{
    long long int r,t,n,a,p,i,j,k,x,y,count=0;
    cin>>t;
    while(t--)
    {
		cin>>a>>n>>p;
		r = a%p;
		for(i=2;i<=p;i++)
		{
			r = pow(r,i)%p;
		}    	
		cout<<rem<<endl;
    }
    return 0;
}
