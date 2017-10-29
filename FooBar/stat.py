for _ in range (input()) :
	n = input()
	l = n-1
	r = n+1
	md = n+1
	s,t = "",""
	j = n+1
	for i in range (n) :
		s += str(j) + " "
		j -= 1
	print s
