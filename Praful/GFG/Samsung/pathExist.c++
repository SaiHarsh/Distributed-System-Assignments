#include <bits/stdc++.h>
using namespace std;
int n, a[1000][1000];
struct point 
{
	int x;
	int y;
};

bool valid (int row, int col)
{
	return (row >= 0) && (row < n) && (col >= 0) && (col < n);
}

int bfs (point src, point dest)
{
	if (src.x == dest.x && src.y == dest.y)
		return true;

	bool visit [n+1][n+1], i;
	int rowN[] = {-1, 0, 0, 1};
	int colN[] = {0, -1, 1, 0};
	//cout << src.x << endl;
	memset (visit, false, sizeof (visit));
	queue <point> q;
	q.push (src);
	visit [src.x][src.y] = true;
	while (!q.empty())
	{
		//cout << dest.x << endl;
		point curr = q.front();
		if (a[curr.x][curr.y] == 2)
			return true;
		//cout << curr.x << " "<< curr.y << endl;
		q.pop();
		for (int j = 0; j < 4; j++)
		{
			
			int row = curr.x + rowN[j];
			int col = curr.y + colN[j];
			if (valid(row, col) && a[row][col] != 0 && !visit[row][col])
			{
				visit[row][col] = true;
				point addCell = {row, col};
				q.push (addCell);
			}
		}
		
	}
	return false;
}
int main()
{
	int t, i, j;
	cin >> t;
	while (t--)
	{
		cin >> n;
		point src, dest;
		for (i = 0; i < n ;i++)
		{
			for (j = 0; j < n ; j++)
			{
				cin >> a[i][j];
				if (a[i][j] == 1){
					 src.x = i; src.y = j;}
				if (a[i][j] == 2){
					 dest.x = i; dest.y= j;}
			}
		}
		if (bfs (src, dest) == true)
			cout << "Yes" << endl;
		else 
			cout << "No" << endl;
	}
	return 0;

}

