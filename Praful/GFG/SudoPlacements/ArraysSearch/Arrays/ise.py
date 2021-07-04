for _ in range (input()) :
	n = input()
	a = map(int, raw_input().split())
	s = ""
	for i in range (n-1) :
		if a[i] > a[i+1] :
			s += str(a[i+1]) + " "
		else :
			s += "-1" + " "
	s += "-1"
	print s
