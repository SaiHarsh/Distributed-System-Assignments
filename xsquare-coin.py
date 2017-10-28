# kadane algorithm
for _ in range (input()) :
	n, k = map(int, raw_input().split())
	l = map(int, raw_input().split())
	s = []
	if l[0] <= k :
		s.append(l[0])
	else :
		s.append(0)
	for i in range (1,n) :
		if l[i] <= k :
			s.append(s[i-1] + l[i])
		else :
			s.append(0)
	s.sort()
	print s[len(s)-1]
