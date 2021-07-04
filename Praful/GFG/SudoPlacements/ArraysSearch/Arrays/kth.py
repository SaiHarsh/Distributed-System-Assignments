for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	k = int(input())
	p, m = [], []
	for i in range (100000) :
		p.append(0)
	for i in l :
		p[i] = 1
	for i in range (100000) :
		if p[i] == 1 :
			k -= 1
		if k == 0 :
			break
	print (i)

