#include <bits/stdc++.h>
using namespace std;
int n, m, a[1000][1000];
struct point 
{
	int x;
	int y;
};
struct node 
{
	point pt;
	int dst;
};
int valid (int row, int col)
{
	return (row >= 0 ) && (row < n) && (col >= 0) && (col < m);
}



int bfs (point src, point dst)
{
	int rown [] = {-1, 0, 0, 1}, i;
	int coln [] = {0, -1, 1, 0};

	if (!a[src.x][src.y] || !a[dst.x][dst.y])
		return INT_MAX;
	bool visit[n][m];
	memset (visit, false, sizeof (visit));
	queue <node> q;
	node s = {src, 0};
	q.push (s);
	while (!q.empty())
	{
		node curr = q.front();
		point pt = curr.pt;
		if (pt.x == dst.x && pt.y == dst.y)
			return curr.dst;
		q.pop();

		for (i = 0; i < 4; i++)
		{
			int row = pt.x + rown[i];
			int col = pt.y + coln[i];

			if (valid (row, col) && a[row][col] && !visit[row][col])
			{
				visit[row][col] = true;
				node addCell = {{row, col}, curr.dst + 1};
				q.push (addCell);
			}
		}
	}
	return INT_MAX;
}

int main()
{
	int t, s, d, x, y, i, j;
	cin >> t;
	while (t--)
	{
		cin >> n >> m ;
		int dt;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < m; j++)
				cin >> a[i][j];
		}
		cin >> x >> y;
		point src = {0, 0};
		point dst = {x, y};

		dt = bfs (src, dst);
		if (dt != INT_MAX)
			cout << dt << endl;
		else 
			cout << "-1" << endl;
	}
	return 0;
}
