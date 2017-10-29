import math

for _ in range(input()) :
	y = input()
	r = 0
	r = int(math.sqrt(y))
	r += 1
	c = 0
	for i in range (1,701) :
		j = 1
		while j != 0 :
			if r <= 0 :
				break
			if r*r + i > y :
				r -= 1
			else :
				break
		if r <= 0 :
			break
		if r*r + i <= y :
			c += r
		

	print c

