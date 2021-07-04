def maxx (p, k) :
	d = 0
	for i in p :
		if d < i :
			d = i
	return d
for _ in range (int(input())) :
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	s = ""
	for i in range (n-k+1) :
		p = maxx(l[i:i+k], k)
		s += str(p)+" "
	print (s)

