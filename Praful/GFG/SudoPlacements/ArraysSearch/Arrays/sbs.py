for _ in range (int(input())) : 
	n = int(input())
	l = list(map(int, input().split()))
	mn, mx = l[0], l[0]
	p = 0
	o = []
	mnI, mxI = 0, 0
	for i in range (1, n) :
		k = mx - mn
		if mn >= l[i] :
			p += abs(mx - mn)
			mn = l[i]
			s = str(mnI) + " " + str(mxI)
			o.append(s)
			mnI = i
			mxI = i
			mx = mn
		elif mx < l[i] :
			mx = l[i]
			mxI = i
		elif k > (l[i]- mn) :
			mn = l[i]
			p += (mx - mn)
			s = str(mnI)+" "+str(mxI)
			o.append(s)
			mx = mn
			mnI, mxI = i, i
	if mnI != mxI :
		o.append(str(mnI)+ " "+str(mxI))
	s = ""
	c = 0
	for i in o :
		x, y = map(int, i.split())
		if x != y :
			s += "("+i+")" + " "
			c += 1
	if c == 0 :
		print "No Profit"
	else :
		print (s)
