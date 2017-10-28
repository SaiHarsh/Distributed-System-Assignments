in = input ()
l,k = [],[]
c = 0
for i in range (101) :
	l.append(0)
for i in range (n) :
	a = input()
	l[a] += 1

for i in range (101) :
	if l[i] == n/2 :
		c += 1
		k.append(i)
		
if c == 2 :
	print "YES"
	print k[0],k[1]
else :
	print "NO"
