import math
for _ in range (int(input())) :
	n = int(input())
	l = list(map(int, input().split()))
	f = 0
	for i in range (n) :
		for j in range (i+1, n) :
			s = (i*i) + (j*j)
			s = math.sqrt(s)
			if s in l :
				f = 1
				break
		if f == 1 :
			break
	if f == 1 :
		print ("yes")
	else :
		print ("No")

