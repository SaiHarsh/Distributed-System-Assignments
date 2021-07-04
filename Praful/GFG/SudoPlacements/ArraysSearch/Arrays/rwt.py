def left (x, y, l) :
	p = l[x:y]
	s = 0
	for i in p :
		if i > s :
			s = i
	return s
def grt (a, b) :
	if a > b :
		return 0
	else:
		return abs(a-b)
for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	opt = min(l[0], l[n-1])
	c = 0
	u = ""
	for i in range (1,n-1) :
		lft = left (0, i, l)
		rft = left (i+1, n, l)
		a = grt (l[i] , lft)
		b = grt (l[i] , rft)
		c += min(a, b)
		#u += str () + " "
	print (c)
