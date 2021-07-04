def printf (l) :
	s = ""
	for i in l :
		s += str(i)
	return s
if __name__ == '__main__' :
	for _ in range (input()) :
		n = input()
		sz = n*2
		curr = 0
		l, r, k = [], [], []
		for i in range (n) :
			k = []
			for j in range (sz - 1) :
				k.append(0)
			r.append(k)

		for i in range (n) :
			l.append(n-i)
		for i in range (2, n+1) :
			l.append(i)
		t = 0

		while t < n : 
			for i in range (sz-1) :
				if l[i] == t :
					l[i] += 1
				r[t][i] = l[i];
			t += 1

		i = n
		y = ""
		while i > 0 :
			y += printf (r[i-1])+ " "
			i -= 1
		for i in range (1,n) :
			y += printf (r[i]) + " "
		print y


