for _ in range (input()) :
	n = input()
	l = map(int,raw_input().split())
	p = "3 4 1 2 6 5"
	top,r,k = [],[],[]
	for i in range (7) :
		top.append(0)
		r.append(0)
	if n == 0 :
		print p
	elif n == 1 :
		print p
	elif n == 2 :
		top[1] = l[0]
		top[2] = l[1]
		if l[0] == l[1] :
			print "-1"
		else :
			for i in range (1,7) :
				if i != top[1] and i != top[2] :
					r[top[1]] = i
					r[i] = top[1]
					break
			for i in range (1,7) :
				if i != top[2] and i not in r :
					r[top[2]] = i
					r[i] = top[2]
					break
			for i in range (1,7) :
				if i not in r :
					k.append(i)
			r[k[0]] = k[1]
			r[k[1]] = k[0]
			h = ""
			for i in range(1,7) :
				h = h + str(r[i]) + " "
			print h
	else :
		print p



