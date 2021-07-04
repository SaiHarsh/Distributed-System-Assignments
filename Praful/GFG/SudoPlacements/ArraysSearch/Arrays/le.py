for _ in  range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	l = l[::-1]
	p = l[0]
	m, s = [p], ""
	for i in range (n) :
		if l[i] > p :
			m.append(l[i])
			p = l[i]
	m = m[::-1]
	for i in m :
		s += str(i) + " "
	print (s)

