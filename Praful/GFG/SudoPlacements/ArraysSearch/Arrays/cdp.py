for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	k = int(input()) - 1
	l.sort()
	i = 0
	s = 100000
	while i < n-k :
		p = l[i+k] - l[i]
		print (l[i], l[i+k], i)
		if p < s :
			s = p
		i += 1
	print (s)
