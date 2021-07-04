#include <bits/stdc++.h>
using namespace std;
struct trie 
{
	struct trie *child[26];
	bool end;
};

struct trie *getHead()
{
	int i;
	struct trie *tmp = (struct trie*)malloc(sizeof(struct trie));
	tmp -> end = false;
	for (i = 0; i < 26; i++)
		tmp->child[i] = NULL;
	return tmp;
}

void insert (struct trie *head, string key)
{
	struct trie* tmp = head;
	for (int i = 0; i < key.length(); ++i)
	{
		int index = key[i]-'a';
		if (!tmp->child[index])
			tmp->child[index] = getHead();
		tmp = tmp->child[index]; 
	}
	tmp->end = true;
}

bool search(struct trie* head, string key)
{
	struct trie* tmp = head;
	for (int i = 0; i < key.length(); ++i)
	{
		int index = key[i] - 'a';
		if (!tmp->child[index])
			return false;
		tmp = tmp->child[index];
	}
	return (tmp != NULL && tmp->end);
}

int main()
{
	string a[100], x;
	int n, i;
	struct trie *head = getHead();
	cin >> n;
	for (i = 0; i < n; ++i)
	{
		cin >> a[i];
	}
	for (i = 0; i < n; i++)
		insert (head, a[i]);

	cin >> x;
	cout << search(head, x) << endl;
	return 0;
}