for _ in range (input()) :
	n, k = map(int,raw_input().split())
	l = map(int, raw_input().split())
	l.sort()
	n = (n+k)/2
	print l[n]
