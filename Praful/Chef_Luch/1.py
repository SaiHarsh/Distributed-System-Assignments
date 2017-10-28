for _ in range (input()) :
	a,b,c,d,e, = 0,0,0,0,0
	for __ in range (input()) :
		s = raw_input().strip()
		if s == "cakewalk" :
			a = 1
		elif s ==  "simple" :
			b = 1
		elif s == "easy" :
			c = 1
		elif s == "easy-medium" or s ==  "medium" :
			d = 1
		elif  s == "medium-hard" or s == "hard" :
			e = 1
	if a == 1 and b == 1 and c == 1 and d == 1 and e == 1 :
		print "Yes"
	else :
		print "No"



	
