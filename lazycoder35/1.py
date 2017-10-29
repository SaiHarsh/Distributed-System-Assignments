n, r = raw_input().split()
n = n.strip()
flag = 1
while len(n) > 1 :
	s = 0
	for i in n :
		s += int(i)

	if flag == 1 :
		s *= int(r)
		flag = 0
	
	n = str(s)
	n = n.strip()
print s
