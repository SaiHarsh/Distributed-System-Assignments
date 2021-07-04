if __name__ == '__main__' :
	for _ in range (int(input())) :
		n = int(input())
		l = list(map(int, input().split()))
		s = -100000
		c = 0
		for i in range (n) :
			p = l[i]
			for j in range (i+1, n) :
				if p <= l[j] :
					p = l[j]
					continue
				else :
					break
			c = abs(i-j)
			if s < c :
				s = c
		print (s)
