def jp(x) :
	s = str(x)
	s = s.strip()
	for i in range (len(s)-1) :
		if abs(int(s[i])-int(s[i+1])) != 1 :
			return 0
	return 1
l = []
for i in range (100000) :
	l.append(jp(i))

for _ in range (int(input())) :
	n = int(input())
	s = ""
	p = []
	for i in range (n) :
		if l[i] == 1 :
			p.append(str(i))
	for i in "0123456789" :
		for j in p :
			if i == j[0] :
				s += j + " "
	print (s)

