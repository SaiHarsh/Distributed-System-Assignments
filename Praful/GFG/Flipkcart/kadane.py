if __name__ == '__main__' :
	for _ in range(input()) :
		n = input()
		l = map(int, raw_input().split())
		k = -100000
		s = 0
		for i in l :
			s += i
			if k < s :
				k = s
			if s < 0 :
				s = 0
		print k
