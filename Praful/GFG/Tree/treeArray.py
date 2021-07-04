def preorder (tree, x, sz) :
	if x < sz :
		print (tree[x]),
		preorder (tree, 2*x + 1, sz)
		preorder (tree, 2*x + 2, sz)

def postorder (tree, x, sz)  :
	if x < sz :
		postorder (tree, 2*x + 1, sz)
		postorder (tree, 2*x + 2, sz)
		print (tree[x]),
	
def inorder (tree, x, sz) :
	if x < sz :
		inorder (tree, 2*x + 1, sz)
		print (tree[x]),
		inorder (tree, 2*x + 2, sz)

def levelorder (tree, x, sz, level) :
	if x >= sz : 
		return
	if level == 1  :
		print tree[x],
	elif level > 1 :
		levelorder (tree, 2*x + 1, sz, level - 1)
		levelorder (tree, 2*x + 2, sz, level - 1)

def height (tree, x, sz) :
	if x >= sz :
		return 0
	else :
		ldepth = height (tree, 2*x + 1, sz)
		rdepth = height (tree, 2*x + 2, sz)
		if ldepth > rdepth :
			return ldepth + 1
		else :
			return rdepth+1

def mirror (tree, x, sz) :
	  if x < sz :
		  mirror (tree, 2*x + 1, sz)
		  mirror (tree, 2*x + 2, sz)
		  l, r = 2*x+1, 2*x+2
		  tree[l], tree[r] = tree[r], tree[l]

if __name__ == '__main__' :
	p = ["exit","pre", "post", "in", "level", "height", "mirror"]
	for i in range (7) :
		print str(i) +" "+p[i]
	print "n : "
	n = input()
	print "tree : "
	tree = map(int, raw_input().split())

	size = len(tree)
	while n != 0 :
		if n == 1 :
			preorder (tree, 0, size)
		elif n == 2 :
			postorder (tree, 0, size)
		elif n == 3 :
			inorder (tree, 0, size)
		elif n == 4 :
			h = height (tree, 0, size)
			for i in range (1, h+1) :
				levelorder (tree, 0, size, i)
		elif n == 5 :
			height (tree, 0, size)
		elif n == 6 :
			mirror (tree, 0, size)
		print ("n :")
		n = input()



