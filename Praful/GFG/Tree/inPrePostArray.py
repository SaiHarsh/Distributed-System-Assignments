def printPost (l, x, n) :
	if x < n :
		#print (x)
		printPost (l, 2*x + 1, n) 
		printPost (l, 2*x + 2, n)
		print (l[x]),

l = map(int, raw_input().split())
n = len(l)
printPost(l, 0, n)
