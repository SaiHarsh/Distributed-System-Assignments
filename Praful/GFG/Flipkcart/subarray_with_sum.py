for _ in range (int(input())) :
	n, k = map(int, input().split())
	l = list(map(int, input().split()))
	ans, s, e = 0, 0, 0
	for i in range (n) :
		if ans == k :
			break
		if k > l[i]+ans :
			ans += l[i]
			e = i
		elif k < l[i]+ans :
			ans += l[i]
			while ans > k :
				ans -= l[s]
				s += 1
			e = i
		else :
			e = i
			ans += l[i]
			break
	if ans == k :
		print (s, e)
	else :
		print ("-1")


