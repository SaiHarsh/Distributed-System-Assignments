#include <bits/std++.h>
using namespace std;
struct node
{
	struct node* child[26];
	bool end;
};

struct node* getHead()
{
	struct node* tmp = (struct node*)malloc(sizeof(struct node));
	tmp->end = false;
	for (int i = 0; i < 26; i++)
		tmp->child[i] = NULL;
	return tmp;
}

void insert(string y, struct node* head)
{
	struct node* tmp = head;
	for (int i = 0; i < y.length(); i++)
	{
		int index = y[i]-'a';
		if (!child[index])
			tmp->child[index] = getHead();
		tmp = tmp->child[index];
	}
	tmp->child[index] = true;
}

bool search (string y, struct node* head)
{
	struct node* tmp = head;
	for (int i = 0; i < y. length(); i++)
	{
		int index;
		if (y[i] == '.')
		{
			for (int j = 0; j < 26; j++)
			{

			}
		}
		else 
		{
		}
	}
	return ;
}


int main()
{
	int i, j, n, q;
	string a[100];
	cin >> n;
	for (i = 0; i < n; i++)
		cin >> a[i];
	cin >> q;
	while (q--)
	{
		cin >> x >> y;
		if (x == 1)
			insert (y, head);
		else 
			cout << search (y, head);
	}
	return 0;
}
