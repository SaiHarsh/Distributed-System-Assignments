for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	k = int(input())
	i = 0
	s = ""
	m = []
	while i < n :
		if i+k < n :
			p = l[i:i+k]
			p = p[::-1]
			m += p
		else :
			p = l[i:]
			p = p[::-1]
			m += p
		i += k
	for i in m :
		s += str(i) + " "
	print (s)

