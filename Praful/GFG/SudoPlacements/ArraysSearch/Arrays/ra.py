for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	k = int(input())
	m, s = [], ""
	for i in range (k, n) :
		m.append(l[i])
	for i in range (k) :
		m.append(l[i])
	for i in m :
		s += str(i)
	print (s)
