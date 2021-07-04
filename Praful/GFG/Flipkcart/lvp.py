for _ in range (int(input())) :
	s = input().strip()
	c, ret, l = 0, 0, []

	for i in s :
		if i == "(" :
			l.append(c)
			c = 0
		elif i == ")" and len(l) > 0:
			c += l.pop() + 2
			ret = max(ret, c)
		elif i == ")" and len(l) == 0:
			c = 0
	
	print (ret)
	
