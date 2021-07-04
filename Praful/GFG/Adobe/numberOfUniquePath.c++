#include <bits/stdc++.h>
using namespace std;
int n, m;
int a[1000][1000];
struct point 
{
	int x;
	int y;
};

bool valid (int row, int col)
{
	return (row >= 0 && row < n && col >= 0 && col < n);
}

int bfs (point src, point dest)
{
	bool visit[n][m];
	memset (visit, false, sizeof (visit));
	int i, j, c = 0;
	int rowN[] = {-1, 0, 0, 1};
	int colN[] = {0, -1, 1, 0};
	queue<point> q;
	q.push (src);
	visit[src.x][src.y] = true;
	while (!q.empty())
	{
		point curr;
		curr = q.front();
		// printf("(%d,%d) ==> %d",curr.x, curr.y, q.size());
		q.pop();
		if (curr.x == dest.x && curr.y == dest.y)
			c += 1;
		for (i = 0; i < 4; i++)
		{
			int row = curr.x + rowN[i];
			int col = curr.y + colN[i];
			if (row == dest.x && col == dest.y)
				q.push({row, col});
			else if (valid (row, col) && !visit[row][col] && !a[row][col])
			{
				point add = {row, col};
				q.push (add);
				visit[row][col] = true;
			}
		}
	}
	return c;
}

int main()
{
	int i, j, dist;
	cin >> n >> m;
	
	for (i = 0; i < n; i++)
	{
		for (j = 0; j < m; j++)
			cin >> a[i][j];
	}
	point src = {0, 0};
	point dest = {n-1, m-1};
	
	cout << bfs (src, dest) << endl;
	return 0;
}
